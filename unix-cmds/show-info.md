### Show disks and Volumes

#### Pi

With no USB drive or anything.

- **df**

```
pi@raspberrypi:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        30G  1.1G   27G   4% /
devtmpfs        460M     0  460M   0% /dev
tmpfs           464M     0  464M   0% /dev/shm
tmpfs           464M   24M  441M   6% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           464M     0  464M   0% /sys/fs/cgroup
/dev/mmcblk0p1   44M   23M   22M  51% /boot
tmpfs            93M     0   93M   0% /run/user/1000
```

- **lsblk**

```
pi@raspberrypi:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
mmcblk0     179:0    0 29.7G  0 disk 
├─mmcblk0p1 179:1    0 43.9M  0 part /boot
└─mmcblk0p2 179:2    0 29.7G  0 part /
```

- **fdisk**

```
pi@raspberrypi:~ $ sudo fdisk -l /dev/mmcblk0
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

Notice that the FAT32 partition is only 43.9M and the Linux partition has expanded to take all the rest of the disk space.

#### Mac

```
> diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *251.0 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                 Apple_APFS Container disk1         250.1 GB   disk0s2
   3:       Apple_KernelCoreDump                         655.4 MB   disk0s3

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +250.1 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            195.8 GB   disk1s1
   2:                APFS Volume Preboot                 42.0 MB    disk1s2
   3:                APFS Volume Recovery                517.0 MB   disk1s3
   4:                APFS Volume VM                      1.1 GB     disk1s4

```