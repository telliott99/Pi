#### mount and unmount or umount

TL;DR

On the Pi, a USB drive is *not* automatically mounted.  You need to 

```
sudo mkdir /mnt/usb
sudo mount /dev/sda1 /mnt/usb
```

More [here](https://www.raspberrypi.org/documentation/configuration/external-storage.md), including auto-mounting.  [wikipedia](https://en.wikipedia.org/wiki/Mount_(computing))

> Mounting is a process by which the operating system makes files and directories on a storage device (such as hard drive, CD-ROM, or network share) available for users to access via the computer's file system.

> In general, the process of mounting comprises operating system acquiring access to the storage medium; recognizing, reading, processing file system structure and metadata on it; before registering them to the virtual file system (VFS) component.

> The exact location in VFS that the newly-mounted medium got registered is called mount point

#### Mac

Volumes or partitions are independent organizational components on a disk, which may have different file systems.

For read/write access a partition must be mounted.  This happens automatically when a USB drive is inserted.  

```
> ls /Volumes/
..	USB128
```

``mount`` by itself shows all mounted volumes.

```
> mount
..
/dev/disk2s1 on /Volumes/USB128 (msdos, local, nodev, nosuid, noowners)
```

If I do ``unmount``

```
> diskutil unmount /dev/disk2s1
Volume USB128 on disk2s1 unmounted
> 
```

Then the USB drive no longer shows up in ``/Volumes`` and there's no way to read/write it.  Re-mount

```
> diskutil mount /dev/disk2s1
Volume USB128 on /dev/disk2s1 mounted
> touch /Volumes/USB128/x
> ls /Volumes/USB128/x
/Volumes/USB128/x
>
```

It's confusing, but both disks and individual volumes can be mounted and unmounted.  

```
> diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
``` 

Use the ``unmountDisk`` command to do that.

In addition to ``hdiutil`` and ``diskutil`` the Mac also has ``fdisk`` and ``df`` but not ``lsblk``.

#### Pi

The Pi doesn't have ``hdiutil`` and ``diskutil``.

On the Pi, it's only ``umount`` with no ``n``.

-  ``sudo umount /dev/sda1``


```s
pi@raspberrypi:~ $ fdisk -l
..
Disk /dev/ram15: 4 MiB, 4194304 bytes, 8192 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes


Disk /dev/mmcblk0: 29.7 GiB, 31914983424 bytes, 62333952 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2f8b6d7b

Device         Boot Start      End  Sectors  Size Id Type
/dev/mmcblk0p1       8192    98045    89854 43.9M  c W95 FAT32 (LBA)
/dev/mmcblk0p2      98304 62333951 62235648 29.7G 83 Linux
```

A bunch of 4 MB "disks" in RAM and then the USB drive from which the Pi was booted.

