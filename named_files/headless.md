Erase the USB drive, format as FAT32 and then

```
> diskutil list
..
/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *30.8 GB    disk2
   1:                 DOS_FAT_32 TE                      30.8 GB    disk2s1

> diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
```

Go to the directory with the .img file.  This has been modified as described [here](../files/15.md).

```
> cd Downloads-saved/Stretch-Lite
> ls
2018-11-13-raspbian-stretch-lite.img	2018-11-13-raspbian-stretch-lite.zip
```

Carefully:

```
> sudo dd bs=1m if=2018-11-13-raspbian-stretch-lite.img of=/dev/rdisk2 conv=sync
Password:
1780+0 records in
1780+0 records out
1866465280 bytes transferred in 39.859892 secs (46825648 bytes/sec)
```

and

```
> sudo diskutil eject /dev/rdisk2
Disk /dev/rdisk2 ejected
> 
```

Insert the disk in the Pi and power up.  Wait 2 min.  Meanwhile, on the Mac, edit ``~/.sshknown_hosts`` to remove 10.0.1.7.

Then

```
> ssh pi@10.0.1.7
pi@10.0.1.7's password: 
```

Ah...

I failed to modify the disk image to contain my RSA public key.  Get in with the password:  ``raspberry``.

A simple fix:  copy over the modified ``sshd_config`` [file](../code/sshd_config):

```
> scp sshd_config pi@10.0.1.7:~
```

On the Pi:

```
pi@raspberrypi:~ $ sudo mv sshd_config /etc/ssh/sshd_config
pi@raspberrypi:~ $ sudo shutdown -r no
```

or just restart the ssh server.  Uhh.. well you could shut it down, but then you'd be kicked off and couldn't restart it  :)

Wait a minute..  On the Mac

```
> ssh pi@10.0.1.7
Last login: Wed Feb 20 15:19:24 2019 from 10.0.1.4
pi@raspberrypi:~ $
```

we're good.

#### RSA key

I don't know a way to provide the RSA Public keyfile in the boot partition.  Some say it's not officially supported, [here](https://www.raspberrypi.org/forums/viewtopic.php?t=212480) are some ideas.

Alternatively we could edit the USB drive (mounted, not booted from) to contain it, and then clone it.  I explore that elsewhere.