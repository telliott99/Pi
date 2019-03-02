I made my own utility to find where a block of null bytes starts.  For convenience, process 16 bytes at a time, and we stop at the first place where there are all null bytes in the read.

This sets up z.bin with 1024 random bytes followed by 1024 null bytes.

```
> dd bs=1024 count=1 if=/dev/random of=z.bin conv=sync
1+0 records in
1+0 records out
1024 bytes transferred in 0.000094 secs (10900932 bytes/sec)
> dd bs=1024 count=1 if=/dev/zero conv=sync >>z.bin
1+0 records in
1+0 records out
1024 bytes transferred in 0.001847 secs (554404 bytes/sec)
```

Look with ``hexdump``:
> hexdump z.bin
0000000 80 42 de a2 d9 f9 fc 20 80 42 68 8b 93 21 84 d3
0000010 20 67 ba b7 4f 25 cb 0b e8 0f a7 ea f3 7b 00 8d
..
00003f0 ce b4 54 97 04 a6 33 dc 50 75 a6 a7 88 33 56 1c
0000400 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
*
0000800
> 

The output from ``reader`` looks like this:

```
z.bin
 80 42 de a2 d9 f9 fc 20 80 42 68 8b 93 21 84 d3   16
 20 67 ba b7 4f 25 cb  b e8  f a7 ea f3 7b  0 8d   32
 ..
 e8 6b fb a2 eb 91 e0 1e d7 f1 ed bd f4 79 92 ac 1008
 ce b4 54 97  4 a6 33 dc 50 75 a6 a7 88 33 56 1c 1024
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 1040
> 

```

We print the next 16 bytes too after checking that we're not past the end.

The code is [here](files/reader.c).

Unfortunately, it doesn't do what I want with our disk image files:

```
> reader 2018-02-26/lite-pub-usb.img 
 fa b8  0 10 8e d0 bc  0 b0 b8  0  0 8e d8 8e c0   16
 fb be  0 7c bf  0  6 b9  0  2 f3 a4 ea 21  6  0   32
  0 be be  7 38  4 75  b 83 c6 10 81 fe fe  7 75   48
 f3 eb 16 b4  2 b0  1 bb  0 7c b2 80 8a 74  1 8b   64
 4c  2 cd 13 ea  0 7c  0  0 eb fe  0  0  0  0  0   80
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0   96
> 
```

We run into null bytes right away!

#### Second attempt

I changed the reader to report transitions and continue:

```
> gcc reader2.c -o reader2 && ./reader2 z.bin
z.bin
 ce b4 54 97  4 a6 33 dc 50 75 a6 a7 88 33 56 1c         1024
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0         1040
1 found
```

when run on our disk image

```
> ./reader ~/Downloads-saved/2018-02-26/lite-pub-usb.img > results.txt
> stat -f %z results.txt
163506480
> 
```

The number of transitions overflowed a signed int!!  1318600 results, the file size was 163.5 MB.

And, the last four results were:

```
2621390944
 a4 96 24 73  1  0 19 50 a2 d8 40  0  0  0  0  0   2621395024
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0   2621395040
 3f 72 44  0  0  0  0  0  0  0  0  0  0  0  0  0   2621404720
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0   2621404736
 4c 47 50 4c 2e  a  0  0  0  0  0  0  0  0  0  0   2621408512
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0   2621408528
 65 79 40 61 6c 65 6b 73 65 79 2e 63 6f 6d 3e  a   2621411536
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0   2621411552
```

They extend essentially to the end of the disk image.  

Maybe what is happening is that the USB drive on which this was written already had sparse data that survived?

Or maybe I got the size just right!

```
> stat -f %z ~/Downloads-saved/2018-02-26/lite-pub-usb.img
2621440000
```

In any event, this approach seems to have failed in a spectacular fashion.

The sensible solution is to let the Pi tell us the number of bytes 

```
pi@raspberrypi:~ $ sudo fdisk -l /dev/sda
Disk /dev/sda: 28.7 GiB, 30752636928 bytes, 60063744 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x78805bfa

Device     Boot Start     End Sectors  Size Id Type
/dev/sda1        8192   98045   89854 43.9M  c W95 FAT32
/dev/sda2       98304 3906250 3807947  1.8G 83 Linux
```

[to do:  real example]

For this example (which is not ``lite-pub-usb.img``), the number of bytes is exactly 2 GB.  So it's probably enough to 5% more or so.  Or try trimming it exactly.

```
>>> 512 * 3906250
2000000000
``` 