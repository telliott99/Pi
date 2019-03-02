Note:  this time, I resized the Linux partition using ``parted``.  This turns out not to be necessary.

#### Making a backup

To start, I tried erasing my 32 GB Sandisk USB drive on the Pi, but ran into trouble.  

Rather than solve that problem now, just eject it (from the desktop) and reformat as FAT32 on the Mac using Disk Utility.  

Boot the Pi with the USB drive plugged in.  From the Mac:

```
> ssh pi@10.0.1.7
Last login: Thu Feb 21 22:01:06 2019
pi@raspberrypi:
```
Now, take a look at what's there with ``lsblk``, ``df -h`` and ``sudo fdisk -l /dev/sda``.  The USB drive is ``/dev/sda`` mounted at ``/media/pi/TE``.  ``lsblk`` gives, in part

```
sda           8:0    1 28.7G  0 disk 
└─sda1        8:1    1 28.7G  0 part /media/pi/TE
```

The USB drive is ``sda``.  ``df -h``

```
pi@raspberrypi:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
..
/dev/mmcblk0p5   30M  398K   28M   2% /media/pi/SETTINGS
/dev/sda1        29G  1.7M   29G   1% /media/pi/TE
```

It is mounted at ``/media/pi``.  I believe ``SETTINGS`` is probably the Master Boot Record.

```
pi@raspberrypi:~ $ sudo fdisk -l /dev/sda
Disk /dev/sda: 28.7 GiB, 30752636928 bytes, 60063744 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start      End  Sectors  Size Id Type
/dev/sda1        2048 60063743 60061696 28.7G  b W95 FAT32
```

#### Grabbing the image

We could go to the website, or we can just copy over the image we have.  Try the latter first.

```
> scp ~/Downloads-saved/Stretch-Lite/2018-11-13-raspbian-stretch-lite.zip pi@10.0.1.7:~/Desktop
2018-11-13-raspbian-stretch-lite.zip                       100%  351MB   7.3MB/s   00:48    
> 
```

We don't have that much space, ``unzip`` and ``rm`` the original file.

```
pi@raspberrypi:~ $ cd Desktop/
pi@raspberrypi:~/Desktop $ ls
2018-11-13-raspbian-stretch-lite.zip
pi@raspberrypi:~/Desktop $ unzip -t 2018-11-13-raspbian-stretch-lite.zip Archive:  2018-11-13-raspbian-stretch-lite.zip
    testing: 2018-11-13-raspbian-stretch-lite.img   OK
No errors detected in compressed data of 2018-11-13-raspbian-stretch-lite.zip.
pi@raspberrypi:~/Desktop $ unzip 2018-11-13-raspbian-stretch-lite.zip 
Archive:  2018-11-13-raspbian-stretch-lite.zip
  inflating: 2018-11-13-raspbian-stretch-lite.img  
pi@raspberrypi:~/Desktop $ ls
2018-11-13-raspbian-stretch-lite.img
2018-11-13-raspbian-stretch-lite.zip
pi@raspberrypi:~/Desktop $ rm 2018-11-13-raspbian-stretch-lite.zip
pi@raspberrypi:~/Desktop $ 
```

Everything is a bit slower on the Pi, but it's not too bad.  Note: I thought the default was to erase, but I guess not.

Now to do the copy:

```
pi@raspberrypi:~/Desktop $ sudo umount /dev/sda
umount: /dev/sda: not mountedpi@raspberrypi:~/Desktop $ sudo dd bs=1000000 if=2018-11-13-raspbian-stretch-lite.img of=/dev/sda  conv=sync
1866+1 records in
1867+0 records out
1867000000 bytes (1.9 GB, 1.7 GiB) copied, 155.94 s, 12.0 MB/s
pi@raspberrypi:~/Desktop $ 
```

Let's see if it works!  Shutdown the Pi, power off, remove the SD card, and reboot.  Boots to the login prompt, so login and look around a bit.  Seems to be fine.

#### Reverse the process

ssh back into the Pi.  Erase the .img file that is still on my Desktop.

```
pi@raspberrypi:~/Desktop $ sudo fdisk -l /dev/sda
Disk /dev/sda: 28.7 GiB, 30752636928 bytes, 60063744 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x274a64c8

Device     Boot Start      End  Sectors  Size Id Type
/dev/sda1        8192    98045    89854 43.9M  c W95 FAT32 (LBA)
/dev/sda2       98304 60063743 59965440 28.6G 83 Linux
```

Our basic problem is that the Linux partition (not shown, but it's ``ext4``) has been sized by the Pi at boot to cover the whole 32 GB USB drive.  That's way too big. 

```
pi@raspberrypi:~/Desktop $ df -h
Filesystem      Size  Used Avail Use% Mounted on
..
/dev/sda2        29G  1.1G   26G   4% /media/pi/rootfs
/dev/sda1        44M   23M   22M  51% /media/pi/boot
/dev/mmcblk0p5   30M  398K   28M   2% /media/pi/SETTINGS
```

We are only using about 4% of it.

I'm not sure it's necessary but we are going to resize the Linux partition.

Resize with ``parted`` (partition editor).  We can do this either on the Mac or here on the Pi.  Try the Pi first:

```
pi@raspberrypi:~/Desktop $ sudo umount /dev/sda2
pi@raspberrypi:~/Desktop $ sudo parted /dev/sda2
GNU Parted 3.2
Using /dev/sda2
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print                                                            
Model: Unknown (unknown)
Disk /dev/sda2: 30.7GB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Flags: 

Number  Start  End     Size    File system  Flags
 1      0.00B  30.7GB  30.7GB  ext4

(parted) resizepart                                                       
Partition number? 1                                                       
End?  [30.7GB]? 2G                                                        
Warning: Shrinking a partition can cause data loss, are you sure you want to continue?
Yes/No? yes                                                               
(parted) quit
Information: You may need to update /etc/fstab.

pi@raspberrypi:~/Desktop $
```

Now copy the disk to an .img file.  The trick here is to tell ``dd`` how much data we want with the ``-count`` flag.

```
pi@raspberrypi:~/Desktop $ sudo dd bs=1000000 count=2000 if=/dev/sda of=~/Desktop/backup.img conv=sync
2000+0 records in
2000+0 records out
2000000000 bytes (2.0 GB, 1.9 GiB) copied, 184.262 s, 10.9 MB/s
```

Zip it.

```
pi@raspberrypi:~/Desktop $ gzip backup.img > backup.gz
pi@raspberrypi:~/Desktop $ ls -al .
total 398984
drwxr-xr-x  2 pi pi      4096 Feb 22 11:32 .
drwxr-xr-x 26 pi pi      4096 Feb 22 11:04 ..
-rw-r--r--  1 pi pi         0 Feb 22 11:27 backup.gz
-rw-r--r--  1 pi pi 408548092 Feb 22 11:26 backup.img.gz
```

Huh.  In contrast to the Mac, that ``>`` did nothing here.  And the default is to erase the source.  We have 408 MB.  That's about right.

Erase the USB drive.  Unzip the backup, copy it to the USB drive, and see if it works to boot the Pi.  

```
pi@raspberrypi:~/Desktop $ gunzip backup.img.gz
pi@raspberrypi:~/Desktop $ sudo dd bs=1000000 if=backup.img of=/dev/sda conv=sync
2000+0 records in
2000+0 records out
2000000000 bytes (2.0 GB, 1.9 GiB) copied, 184.116 s, 10.9 MB/s
```

And ... it works!!