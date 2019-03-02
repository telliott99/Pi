This doesn't work (yet).

Suppose we want to do arbitrary stuff on boot
(like loading a public key) [link](https://www.raspberrypi.org/forums/viewtopic.php?t=212480).

**hello**

```
#! /bin/sh
echo "hello"

```

```
> scp hello pi@10.0.1.7:~
hello                 100%   24     7.2KB/s   00:00    
> ssh pi@10.0.1.7
Last login: Fri Feb 22 14:10:07 2019 from 10.0.1.4
pi@raspberrypi:~ $ ls
hello  motd  sshd_config
pi@raspberrypi:~ $ ./hello
hello
pi@raspberrypi:~ $
```

We need to edit ``/boot/cmdline.txt``.  At the end, put

```
init=/path/to/my/script
```

On the Pi:

```
pi@raspberrypi:/boot $ cat /boot/cmdline.txt
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=c5c0c3da-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

```
pi@raspberrypi:/boot $ sudo mkdir start
pi@raspberrypi:/boot $ sudo cp ~/hello start
pi@raspberrypi:/boot $ nano cmdline.txt
pi@raspberrypi:/boot $ sudo nano cmdline.txt
```

```
sudo shutdown -r now
```

I don't see anything.

Possibly it's because we've already expanded the file system, etc.

```
Last login: Fri Feb 22 09:33:21 on console
> cd Desktop
> gunzip backup.img.gz 
> hdiutil attach backup.img 
/dev/disk2          	FDisk_partition_scheme         
/dev/disk2s1        	Windows_FAT_32                 /Volumes/boot
/dev/disk2s2        	Linux                          
> cd /Volumes/boot
> ls
..
cmdline.txt
..
> mkdir te
> cp ~/Desktop/hello te
> cd te
> ./hello
hello
> cd ..
> te/hello
hello
> te cmdline.txt 
[edit to put te/hello at end]
> hdiutil detach /dev/disk2
hdiutil: couldn't unmount "disk2" - Resource busy
> 
```

Just relaunch Terminal.


> diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
> sudo dd bs=1m if=backup.img of=/dev/rdisk2 conv=sync
Password:
2000+0 records in
2000+0 records out
2097152000 bytes transferred in 54.936037 secs (38174432 bytes/sec)
> diskutil eject /dev/disk2
Disk /dev/disk2 ejected
>



