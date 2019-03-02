a graphical [partition editor](https://learn.adafruit.com/resizing-raspberry-pi-boot-partition/edit-partitions) 

The Pi modifies the size of the file system expansion on first boot.  There's a shell script (``/usr/bin/raspi-config``) that calls a binary tool /sbin/resize2fs

> The resize2fs program will resize  ext2,  ext3,
or  ext4  file  systems.   It  can  be  used to
enlarge or  shrink  an  unmounted  file  system
located   on  device.   If  the  filesystem  is
mounted, it can be used to expand the  size  of
the mounted filesystem, assuming the kernel and
the  file  system  supports  on-line  resizing.

#### What we do

The first tool used by most folks is ``lsblk`` (not present on macOS):

```
pi@raspberrypi:~ $ lsblk   
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    1 28.7G  0 disk 
|-sda1   8:1    1 43.9M  0 part /boot
`-sda2   8:2    1 28.6G  0 part /
```

This is the result when the USB drive is the boot drive.

Another one is ``df -h``

```
pi@raspberrypi:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  1.1G   26G   4% /
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M     0  464M   0% /dev/shm
tmpfs           464M  6.2M  458M   2% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/sda1        44M   23M   22M  51% /boot
```

Put the micro SD card back in to boot from and the USB drive in also.

```
pi@raspberrypi:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    1 28.7G  0 disk 
├─sda1        8:1    1 43.9M  0 part /media/pi/boot
└─sda2        8:2    1 28.6G  0 part /media/pi/rootfs
mmcblk0     179:0    0 14.9G  0 disk 
├─mmcblk0p1 179:1    0  1.8G  0 part 
├─mmcblk0p2 179:2    0    1K  0 part 
├─mmcblk0p5 179:5    0   32M  0 part /media/pi/SETTINGS
├─mmcblk0p6 179:6    0   69M  0 part /boot
└─mmcblk0p7 179:7    0   13G  0 part /
pi@raspberrypi:~ $ 
```

You can see that the boot partition has about 43.9M of files.  This the FAT32 partition.

I learned a bit about the "partition editor" [here](https://www.tecmint.com/parted-command-to-create-resize-rescue-linux-disk-partitions/).  It's called ``parted``.


```
pi@raspberrypi:~ $ sudo parted
GNU Parted 3.2
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of
commands.
                                                        (parted) print    
Model: SanDisk Ultra USB 3.0 (scsi)
Disk /dev/sda: 30.8GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      4194kB  50.2MB  46.0MB  primary  fat32        lba
 2      50.3MB  30.8GB  30.7GB  primary  ext4

                                                        (parted)          
```

Resizing is as simple as

```
pi@raspberrypi:~ $ sudo parted
GNU Parted 3.2
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of
commands.
                                                        (parted) resizepart
                                                        Partition number? 2
Warning: Partition /dev/sda2 is being used. Are you sure
you want to continue?
                                                                                                                Yes/No? yes       
                                                        End?  [30.8GB]? 2.0GB
Warning: Shrinking a partition can cause data loss, are
you sure you want to continue?
                                                                                                                Yes/No? yes       
                                                        (parted) quit     
Information: You may need to update /etc/fstab.
                                                       pi@raspberrypi:~ $                                                                                                  ```                                                   

The partition has indeed shrunk:


```
pi@raspberrypi:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    1 28.7G  0 disk 
├─sda1        8:1    1 43.9M  0 part /media/pi/boot
└─sda2        8:2    1  1.8G  0 part /media/pi/rootfs
mmcblk0     179:0    0 14.9G  0 disk 
├─mmcblk0p1 179:1    0  1.8G  0 part 
├─mmcblk0p2 179:2    0    1K  0 part 
├─mmcblk0p5 179:5    0   32M  0 part /media/pi/SETTINGS
├─mmcblk0p6 179:6    0   69M  0 part /boot
└─mmcblk0p7 179:7    0   13G  0 part /
```

b/c

```
└─sda2        8:2    1  1.8G  0 part /media/pi/rootfs
```

but 

```
sda           8:0    1 28.7G  0 disk
```

Maybe that's why it still writes the whole thing.

Check with

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
pi@raspberrypi:~ $
```
                                                  
#### Using a second USB drive

I resized the ext4 partition.  But the disk ``sda`` still shows 28.7G.

The write fails when we hit the 4G limit for FAT32 file size.  It is writing the whole thing.

```
pi@raspberrypi:~ $ sudo dd bs=1024 if=/dev/sda of=/media/pi/F479-AB75/backup.img conv=sync
dd: error writing '/media/pi/F479-AB75/backup.img': File too large
4194304+0 records in
4194303+0 records out
4294967295 bytes (4.3 GB, 4.0 GiB) copied, 317.444 s, 13.5 MB/s
pi@raspberrypi:~ $ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda           8:0    1  28.7G  0 disk 
├─sda1        8:1    1  43.9M  0 part /media/pi/boot
└─sda2        8:2    1   1.8G  0 part 
sdb           8:16   1 114.6G  0 disk 
└─sdb1        8:17   1 114.6G  0 part /media/pi/F479-AB75
mmcblk0     179:0    0  14.9G  0 disk 
├─mmcblk0p1 179:1    0   1.8G  0 part 
├─mmcblk0p2 179:2    0     1K  0 part 
├─mmcblk0p5 179:5    0    32M  0 part /media/pi/SETTINGS
├─mmcblk0p6 179:6    0    69M  0 part /boot
└─mmcblk0p7 179:7    0    13G  0 part /
pi@raspberrypi:~ $ 
```

According to [this](https://ss64.com/bash/dd.html)

> dd

> Convert and copy a file, write disk headers, boot records, create a boot floppy. dd can make an exact clone of an (unmounted) disk, this will include all blank space so the output destination must be at least as large as the input.

which suggests this ain't gonna work.  But wait!  From ``man dd``:

```
bs=n     

Set both input and output block size
to n bytes, superseding the ibs and
obs operands.  If no conversion val-
ues other than noerror, notrunc or
sync are specified, then each input
block is copied to the output as a
single block without any aggregation
of short blocks.

count=n  
Copy only n input blocks.
```

Copy only n blocks!  Test

```
pi@raspberrypi:~ $ sudo dd bs=1000000 count=2 if=/dev/sda of=/media/pi/F479-AB75/backup.img conv=sync
2+0 records in
2+0 records out
2000000 bytes (2.0 MB, 1.9 MiB) copied, 0.117291 s, 17.1 MB/s
```

Do it

```
pi@raspberrypi:~ $ sudo dd bs=1000000 count=2000 if=/dev/sda of=/media/pi/F479-AB75/backup.img conv=sync
2000+0 records in
2000+0 records out
2000000000 bytes (2.0 GB, 1.9 GiB) copied, 149.91 s, 13.3 MB/s
pi@raspberrypi:~ $ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda           8:0    1  28.7G  0 disk 
├─sda1        8:1    1  43.9M  0 part /media/pi/boot
└─sda2        8:2    1   1.8G  0 part 
sdb           8:16   1 114.6G  0 disk 
└─sdb1        8:17   1 114.6G  0 part /media/pi/F479-AB75
mmcblk0     179:0    0  14.9G  0 disk 
├─mmcblk0p1 179:1    0   1.8G  0 part 
├─mmcblk0p2 179:2    0     1K  0 part 
├─mmcblk0p5 179:5    0    32M  0 part /media/pi/SETTINGS
├─mmcblk0p6 179:6    0    69M  0 part /boot
└─mmcblk0p7 179:7    0    13G  0 part /
pi@raspberrypi:~ $ ls /media/pi/F479-AB75/
backup.img                           SanDiskSecureAccess
Back Up Your Files to the Cloud.pdf  SanDiskSecureAccessV3.1_win.exe
pi@raspberrypi:~ $ ls -al /media/pi/F479-AB75/backup.img
-rw-r--r-- 1 pi pi 2000000000 Feb 21 21:12 /media/pi/F479-AB75/backup.img
pi@raspberrypi:~ $ cd /media/pi/F479-AB75/

```

gzip deletes without ``-c``

```
pi@raspberrypi:/media/pi/F479-AB75 $ gzip -c backup.img > backup.gz
pi@raspberrypi:/media/pi/F479-AB75 $ ls -al backup.gz
-rw-r--r-- 1 pi pi 409341914 Feb 21 21:30 backup.gz
pi@raspberrypi:/media/pi/F479-AB75 $ 
```

Theoretically, you could pipe from ``dd`` to ``gzip``.

#### Test it

gunzip -c backup.gz > backup.img


I should have, at this point, copied it to the Pi's memory.


pi@raspberrypi:/media/pi/F479-AB75 $ sudo mkdosfs -F 32 -I /dev/sda
mkfs.fat 4.1 (2017-01-24)
mkdosfs: unable to open /dev/sda: Device or resource busy


sudo shutdown now

Had trouble with that so just reformat on Mac

They switched now sdb is 32 GB

sudo dd bs=1024 if=/media/pi/F479-AB75/backup.img of=/dev/sdb conv=sync

/media/pi/F479-AB75/backup.img is gone

restart and file isn't found on big USB drive
