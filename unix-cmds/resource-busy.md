#### Resource busy error

```
> sudo hdiutil unmount /dev/disk2
"/dev/disk2" was already unmounted.
> sudo newfs_msdos /dev/rdisk2 -N
newfs_msdos: /dev/rdisk2: Resource busy
```

[ref](https://unix.stackexchange.com/questions/444740/why-is-this-dd-command-producing-resource-busy-errors)


What is causing this is that the volume disk2s1 is still mounted

```
> df -h
..
/dev/disk2s1    29Gi  1.5Mi   29Gi     1%       0                   0  100%   /Volumes/TE
```

this'll fix it

```
> sudo diskutil unmount /dev/disk2s1
Volume TE on disk2s1 unmounted
```

#### Disk Utility v. the command line

``newfs_msdos`` is to install a new file system, but ``-N`` means we're only looking, so far:

```
> sudo newfs_msdos /dev/rdisk2 -N
512 bytes per physical sector
/dev/rdisk2: 60034368 sectors in 1876074 FAT32 clusters (16384 bytes/cluster)
bps=512 spc=32 res=32 nft=2 mid=0xf0 spt=32 hds=255 hid=0 drv=0x00 bsec=60063744 bspf=14657 rdcl=2 infs=1 bkbs=6
```

The above is after using Disk Utility to erase and reformat as FAT32 MBR I get:

- sector size (bytes):      512
- sectors per cluster:       32   # calculated
- bytes per cluster:      16384
- clusters              1876074
- sectors              60034368

So let's do it

```
> sudo newfs_msdos /dev/rdisk2
512 bytes per physical sector
/dev/rdisk2: 60034368 sectors in 1876074 FAT32 clusters (16384 bytes/cluster)
bps=512 spc=32 res=32 nft=2 mid=0xf0 spt=32 hds=255 hid=0 drv=0x00 bsec=60063744 bspf=14657 rdcl=2 infs=1 bkbs=6
> 
```

Conclusion:

- command line version gives the same result as Disk Utility
- unmount the *Volume* to fix "Resource busy"
