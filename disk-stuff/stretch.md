Raspbian Stretch is the Pi OS with a desktop but not the full load of extra software.

#### Install on a USB drive

```
> cd /Users/telliott_admin/Downloads-saved/Stretch
> ls
2018-11-13-raspbian-stretch.zip
> openssl dgst -SHA256 2018-11-13-raspbian-stretch.zip 
SHA256(2018-11-13-raspbian-stretch.zip)= a121652937ccde1c2583fe77d1caec407f2cd248327df2901e4716649ac9bc97
```

Paste it somewhere

```
a121652937ccde1c2583fe77d1caec407f2cd248327df2901e4716649ac9bc97
```

SHA-256 hash from [download page](https://www.raspberrypi.org/downloads/raspbian/):

```
a121652937ccde1c2583fe77d1caec407f2cd248327df2901e4716649ac9bc97
```

That's a match.  So

```
> unzip -t 2018-11-13-raspbian-stretch.zip 
Archive:  2018-11-13-raspbian-stretch.zip
    testing: 2018-11-13-raspbian-stretch.img   OK
No errors detected in compressed data of 2018-11-13-raspbian-stretch.zip.
> 
```
and

```
> unzip 2018-11-13-raspbian-stretch.zip 
Archive:  2018-11-13-raspbian-stretch.zip
  inflating: 2018-11-13-raspbian-stretch.img  
> ls
2018-11-13-raspbian-stretch.img
2018-11-13-raspbian-stretch.zip
>
```

Erase my USB thumb drive and reformat as FAT32
then

- list
 
```
> diskutil list
/dev/disk0 (internal, physical):
..
/dev/disk1 (synthesized):
..
/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *30.8 GB    disk2
   1:                 DOS_FAT_32 TE                      30.8 GB    disk2s1

> 
```

disk2, as usual

``cd`` to the download:

```
> cd /Users/telliott_admin/Downloads-saved/Stretch
```

- unmount

```
> diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
```

- triple-check the ``of`` (outfile), and copy

```
> sudo dd bs=1m if=2018-11-13-raspbian-stretch.img of=/dev/rdisk2 conv=sync
Password:
3248+0 records in
3248+0 records out
3405774848 bytes transferred in 101.654683 secs (33503374 bytes/sec)
```

- eject

```
> diskutil eject /dev/rdisk2
Disk /dev/rdisk2 ejected
> 
```

Remove the drive.

There does not seem to be any way to tell the Pi to boot preferentially from the USB drive.  

Solution:  remove the SD card, plug in USB and power up.

Boots super-fast, to the Desktop.

```
Raspberry > Preferences > Configuration
```

Set Locale, Country Code.  Toggle SSH service.  Click on the WiFi icon, click on my network, supply password.  Reboot.

From the Mac

```
> ssh pi@10.0.1.7
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:sfwqAb8JLZEozSERXMMSiVnp3zxf9uWrHimpm/zqLs4.
Please contact your system administrator.
Add correct host key in /Users/telliott_admin/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/telliott_admin/.ssh/known_hosts:13
ECDSA host key for 10.0.1.7 has changed and you have requested strict checking.
Host key verification failed.
> 
```

Delete the key for ``10.0.1.7`` from ``known_hosts`` and try again.

```
Last login: Tue Feb 19 09:48:57 on ttys000
cd Desktop
> cd Desktop
> ssh pi@10.0.1.7
The authenticity of host '10.0.1.7 (10.0.1.7)' can't be established.
ECDSA key fingerprint is SHA256:sfwqAb8JLZEozSERXMMSiVnp3zxf9uWrHimpm/zqLs4.
Are you sure you want to continue connecting (yes/no)? yes 
Warning: Permanently added '10.0.1.7' (ECDSA) to the list of known hosts.
pi@10.0.1.7's password: 
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb 19 14:44:06 2019

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@raspberrypi:~ $ 
```

To change to Pubkey Authorization, let's save config page to the Mac and modify it there:

```
> scp pi@10.0.1.7:/etc/ssh/sshd_config .
pi@10.0.1.7's password: 
sshd_config           100% 3298   443.9KB/s   00:00    
> 
```

Edit with TextEdit, exactly as [before](../files/3.md).

```
> scp ./sshd_config pi@10.0.1.7:/home/pi
pi@10.0.1.7's password: 
sshd_config           100% 3294   646.7KB/s   00:00    
>
```

And on the Pi

```
pi@raspberrypi:~ $ sudo cp sshd_config /etc/ssh
```

Now I just need to copy my Public key to the Pi.  

One way, on the Mac:

```
> ssh-copy-id pi@10.0.1.7
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/telliott_admin/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
pi@10.0.1.7's password: 

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'pi@10.0.1.7'"
and check to make sure that only the key(s) you wanted were added.

>
```

and then

```
Last login: Tue Feb 19 09:50:27 on ttys001
cd Desktop
> cd Desktop
> ssh pi@10.0.1.7
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb 19 14:50:37 2019 from 10.0.1.4
pi@raspberrypi:~ $ 
```

I find the extra text annoying.  It is in ``/etc/motd`` according to [this](https://raspberrypi.stackexchange.com/questions/73681/raspberry-pi-custom-ssh-normal-login-message)

```
pi@raspberrypi:~ $ sudo cp /etc/motd /etc/motd.old
pi@raspberrypi:~ $ sudo nano /etc/motd
```
and edit.

Now:

```
> ssh pi@10.0.1.7
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l
Peace and love.
Last login: Tue Feb 19 15:22:07 2019 from 10.0.1.4
pi@raspberrypi:~ $
```

We are good to go.
