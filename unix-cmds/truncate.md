#### Truncate and dd examples

Start with 

```
> echo "abc" > x.txt
> hexdump -C x.txt
00000000  61 62 63 0a                                       |abc.|
00000004
```

then 

```
> sudo dd bs=1024 if=x.txt of=y.txt conv=sync
Password:
0+1 records in
1+0 records out
1024 bytes transferred in 0.000080 secs (12820798 bytes/sec)
> hexdump -C y.txt
00000000  61 62 63 0a 00 00 00 00  00 00 00 00 00 00 00 00  |abc.............|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000400
>
```

We specified a block size of 1024, and what we actually got was ``0x400`` = 256 times 4 = 1024.

```
> stat -f %z y.txt
1024
```

If we know exactly how many bytes we want we can specify ``count``.

A block can be pretty small:

```
> sudo dd bs=16 count=5 if=x.txt of=z.txt conv=sync
0+1 records in
1+0 records out
16 bytes transferred in 0.000044 secs (362751 bytes/sec)
>
```

```
> hexdump -C z.txt
00000000  61 62 63 0a 00 00 00 00  00 00 00 00 00 00 00 00  |abc.............|
00000010
>
```

This [link](https://superuser.com/questions/610819/how-to-resize-img-file-created-with-dd) says that ``gzip`` should compress well.  But it doesn't work at this scale:

```
> gzip -c y.txt > y.txt.gz
> gunzip -c y.txt.gz > yy.txt
> hexdump -C yy.txt
00000000  61 62 63 0a 00 00 00 00  00 00 00 00 00 00 00 00  |abc.............|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000400
> stat -f %z yy.txt
1024
```

Notice the -c and > so gzip and gunzip won't overwrite our source file.

