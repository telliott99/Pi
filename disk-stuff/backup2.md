In the [previous page](backup.md), we tested an approach for making a backup of the Pi OS (and the rest of the file system).  

It mostly uses the Pi, which is a bit slow.  The big points are:

- ``dd`` takes an argument ``count`` that limits the amount of data to copy
- ``parted`` can shrink the Linux partition to a reasonable size (down from 32 GB)

What we want to do here:

- test whether resizing is necessary
- do some of this on the Mac (faster)
- repeat with a copy configured for WiFi and ssh

#### Formatting on the Mac

Plug in the USB drive.

```
/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *30.8 GB    disk2
   1:             Windows_FAT_32 boot                    46.0 MB    disk2s1
   2:                      Linux                         30.7 GB    disk2s2
```

Try just writing the first 2.0 GB with no resizing:

```
> sudo dd bs=1m count=2000 if=/dev/rdisk2 of=~/Desktop/backup.img conv=sync
Password:
2000+0 records in
2000+0 records out
2097152000 bytes transferred in 14.942414 secs (140348942 bytes/sec)
> gzip backup.img
> 
```

``backup.img`` has been erased.

```
> gunzip backup.img.gz -c > backup.img
```

The ``-c`` flag preserves the source, and writes to ``stdout``, hence the ``>``.

```
> sudo diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
> sudo dd bs=1m if=backup.img of=/dev/rdisk2 conv=sync
2000+0 records in
2000+0 records out
2097152000 bytes transferred in 57.026202 secs (36775235 bytes/sec)
> sudo diskutil eject /dev/disk2
Disk /dev/disk2 ejected
>
```

Test it in the Pi:  it works!