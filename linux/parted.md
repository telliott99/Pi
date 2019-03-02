pi@raspberrypi:~/Desktop $ sudo fdisk -l /dev/sda
Disk /dev/sda: 28.7 GiB, 30752636928 bytes, 60063744 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x6a9443da

Device     Boot Start      End  Sectors  Size Id Type
/dev/sda1        8192    98045    89854 43.9M  c W95 FAT
/dev/sda2       98304 60063743 59965440 28.6G 83 Linux

with two partitions

sudo umount /dev/sda


pi@raspberrypi:~/Desktop $ sudo parted /dev/sda
GNU Parted 3.2
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of
commands.
                                                        (parted)          



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



https://www.tecmint.com/parted-command-to-create-resize-rescue-linux-disk-partitions/




pi@raspberrypi:~/Desktop $ sudo parted /dev/sda
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
                                                        (parted) resizepart
                                                        Partition number? 2
Warning: Partition /dev/sda2 is being used. Are you sure
you want to continue?
                                                                                                                Yes/No? yes
                                                        End?  [30.8GB]? 2G
Warning: Shrinking a partition can cause data loss, are
you sure you want to continue?
                                                                                                                Yes/No? yes       
                                                        (parted) print    
Model: SanDisk Ultra USB 3.0 (scsi)
Disk /dev/sda: 30.8GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      4194kB  50.2MB  46.0MB  primary  fat32        lba
 2      50.3MB  2000MB  1950MB  primary  ext4

                                                        (parted) quit
Information: You may need to update /etc/fstab.

                                                         pi@raspberrypi:~/Desktop $

pi@raspberrypi:~/Desktop $ sudo eject /dev/sda



for a GUI

https://learn.adafruit.com/resizing-raspberry-pi-boot-partition/edit-partitions
 


