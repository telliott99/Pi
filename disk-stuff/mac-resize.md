#### Cute idea that didn't work

Resize the original FAT32 partition to 2 GB.  

Use Disk Utility to erase USB drive then

from ``man hdiutil``

> The last partition will be lengthened to the end of the disk; to specify an
exact size for the last usable partition, specify an additional partition
of type "Free Space".

I figured out a command that works:  

```
diskutil partitionDisk /dev/disk2 2 \
MBR MS-DOS TE 2G "Free Space" FOO 0
```

We're asking for two partitions, the second one is of type "Free Space."

```
> diskutil partitionDisk /dev/disk2 2 MBR MS-DOS TE 2G "Free Space" FOO 0
Started partitioning on disk2
Unmounting disk
Creating the partition map
Waiting for partitions to activate
Formatting disk2s1 as MS-DOS (FAT) with name TE
512 bytes per physical sector
/dev/rdisk2s1: 3898608 sectors in 487326 FAT32 clusters (4096 bytes/cluster)
bps=512 spc=8 res=32 nft=2 mid=0xf8 spt=32 hds=255 hid=2048 drv=0x80 bsec=3906256 bspf=3808 rdcl=2 infs=1 bkbs=6
Mounting disk
Finished partitioning on disk2
/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *30.8 GB    disk2
   1:                 DOS_FAT_32 TE                      2.0 GB     disk2s1
>
```

Looks like it worked!

Now copy over the .img for Stretch-Lite

```
> diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
> sudo dd bs=1m if=2018-11-13-raspbian-stretch-lite.img of=/dev/rdisk2 conv=sync
1780+0 records in
1780+0 records out
1866465280 bytes transferred in 38.698417 secs (48231050 bytes/sec)
> sudo diskutil eject /dev/disk2
Disk /dev/disk2 ejected
> 
```

And ...

When the Pi boots it resizes to the whole 32 GB.  Oh well.