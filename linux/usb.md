#### Exploring USB drives for data

Here I'm looking at mounting and writing to a USB drive from the Pi (in contrast to booting the OS from a disk image that's been copied onto a USB drive).

We'll also reformat the drive with a single FAT32 partition.

The Pi was booted from a 32GB micro SD card with my ``lite-pub-sd.img`` installed on it, and with an erased USB drive (formatted as FAT32 w/MBR) also inserted.

I ssh in using the alias ``spi`` which stands for ``ssh pi@10.0.1.7``.

A basic look is provided by ``lsblk``:

```
pi@raspberrypi:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    1 28.7G  0 disk 
`-sda1        8:1    1 28.7G  0 part 
mmcblk0     179:0    0 29.7G  0 disk 
|-mmcblk0p1 179:1    0 43.9M  0 part /boot
`-mmcblk0p2 179:2    0  7.4G  0 part /
```

The USB drive is called ``/dev/sda``.  It would be hard to be sure that this *is* the USB drive, since it's the same size as the card.  I'd prefer to see a name for it.

``df -h | grep "sda"`` gives nothing.  That's not like before.  And it's not mounted (see ``lsblk``).  That's not like before, either.  

#### Mount USB drive

So mount it:

```
pi@raspberrypi:~ $ sudo mkdir /mnt/usb
pi@raspberrypi:~ $ sudo mount /dev/sda1 /mnt/usb
```

```
pi@raspberrypi:/mnt/usb $ lsblk | grep "sda"
sda           8:0    1 28.7G  0 disk 
`-sda1        8:1    1 28.7G  0 part /mnt/usb
pi@raspberrypi:/mnt/usb $ df -h | grep "sda"
/dev/sda1        29G  1.6M   29G   1% /mnt/usb
```

The first (and only) partition is mounted at ``/mnt/usb``.  We can read/write files at this point, by navigating from ``mnt/usb``.

[Note:  the usual mount point on Pi is ``/media/pi``.]

I notice something odd.  This version of the OS was first booted on an 8 GB SD card, and the reboot has not expanded the linux partition to the full size.  We can fix that, as described [here](linux-resize.md).

However, I decided instead to set up the 32 GB card again from ``lite-usb.img`` and using ``setup-pi/go`` as described ___.

```
`-mmcblk0p2 179:2    0  7.4G  0 part /
```

Look around with ``fdisk``:

```
pi@raspberrypi:/mnt/usb $ sudo fdisk /dev/sda

Welcome to fdisk (util-linux 2.29.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk /dev/sda: 28.7 GiB, 30752636928 bytes, 60063744 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start      End  Sectors  Size Id Type
/dev/sda1        2048 60063743 60061696 28.7G  b W95 FAT32

Command (m for help): 
```

#### Delete the old partition(s) and make a new one

```
pi@raspberrypi:/mnt/usb $ sudo fdisk /dev/sda

Welcome to fdisk (util-linux 2.29.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk /dev/sda: 28.7 GiB, 30752636928 bytes, 60063744 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000

Device     Boot Start      End  Sectors  Size Id Type
/dev/sda1        2048 60063743 60061696 28.7G  b W95 FAT32

Command (m for help): d
Selected partition 1
Partition 1 has been deleted.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (1-4, default 1): 
First sector (2048-60063743, default 2048): 
Last sector, +sectors or +size{K,M,G,T,P} (2048-60063743, default 60063743): 

Created a new partition 1 of type 'Linux' and of size 28.7 GiB.
Partition #1 contains a vfat signature.

Do you want to remove the signature? [Y]es/[N]o: yes

The signature will be removed by a write command.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Re-reading the partition table failed.: Device or resource busy

The kernel still uses the old table. The new table will be used at the next reboot or after you run partprobe(8) or kpartx(8).

pi@raspberrypi:/mnt/usb $ 
```

####  Change the type

```
Command (m for help): t
Selected partition 1
Partition type (type L to list all types): L

 0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris        
 1  FAT12           27  Hidden NTFS Win 82  Linux swap / So c1  DRDOS/sec (FAT-
 2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
 3  XENIX usr       3c  PartitionMagic  84  OS/2 hidden or  c6  DRDOS/sec (FAT-
 4  FAT16 <32M      40  Venix 80286     85  Linux extended  c7  Syrinx         
 5  Extended        41  PPC PReP Boot   86  NTFS volume set da  Non-FS data    
 6  FAT16           42  SFS             87  NTFS volume set db  CP/M / CTOS / .
 7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Dell Utility   
 8  AIX             4e  QNX4.x 2nd part 8e  Linux LVM       df  BootIt         
 9  AIX bootable    4f  QNX4.x 3rd part 93  Amoeba          e1  DOS access     
 a  OS/2 Boot Manag 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O        
 b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor      
 c  W95 FAT32 (LBA) 52  CP/M            a0  IBM Thinkpad hi ea  Rufus alignment
 e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         eb  BeOS fs        
 f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ee  GPT            
10  OPUS            55  EZ-Drive        a7  NeXTSTEP        ef  EFI (FAT-12/16/
11  Hidden FAT12    56  Golden Bow      a8  Darwin UFS      f0  Linux/PA-RISC b
12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f1  SpeedStor      
14  Hidden FAT16 <3 61  SpeedStor       ab  Darwin boot     f4  SpeedStor      
16  Hidden FAT16    63  GNU HURD or Sys af  HFS / HFS+      f2  DOS secondary  
17  Hidden HPFS/NTF 64  Novell Netware  b7  BSDI fs         fb  VMware VMFS    
18  AST SmartSleep  65  Novell Netware  b8  BSDI swap       fc  VMware VMKCORE 
1b  Hidden W95 FAT3 70  DiskSecure Mult bb  Boot Wizard hid fd  Linux raid auto
1c  Hidden W95 FAT3 75  PC/IX           bc  Acronis FAT32 L fe  LANstep        
1e  Hidden W95 FAT1 80  Old Minix       be  Solaris boot    ff  BBT            
Partition type (type L to list all types): b
Changed type of partition 'Linux' to 'W95 FAT32'.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

#### Check

Make sure it's correct:

```
pi@raspberrypi:~ $ sudo fdisk -l /dev/sda | grep "sda1"
/dev/sda1        2048 60063743 60061696 28.7G  b W95 FAT32
```

The problem with this before was that I had

```
/dev/sda1        2048 60063743 60061696 28.7G  83 Linux
```

The reason is that after creating a new partition, changing the type to FAT32 is a *separate* step.  So it's:

```
sudo fdisk /dev/sda
..
n  # accept default options
t  # to change type
b  # for FAT32
w  # to write the result
```

and then

```
sudo fdisk -l /dev/sda
```

#### Istall the new file system

```
pi@raspberrypi:~ $ sudo mkfs.fat -F 32 -I /dev/sda1
mkfs.fat 4.1 (2017-01-24)
pi@raspberrypi:~ $ sudo umount /dev/sda 
umount: /dev/sda: not mounted
pi@raspberrypi:~ $ sudo umount /dev/sda1
umount: /dev/sda1: not mounted
```


