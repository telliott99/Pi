#### Modifying a backup or downloaded image

In this section, we will modify the Stretch-Lite image that was downloaded from [here](https://www.raspberrypi.org/downloads/raspbian/), boot it on the Pi to complete the setup, and then save a backup image.

For configuration we need to:

- set Locale and Country Code
- turn on WiFi and set the password
- turn on SSH service
- provide a public key for the user's login
- turn on Pubkey Authorization 

Copying over the keys may be [possible in theory](https://www.raspberrypi.org/forums/viewtopic.php?t=212480), but is not supported.  We leave that for another time.

#### Modifying the image

On the Mac, make a copy of the image.

```
> cp ~/Downloads-saved/Stretch-Lite/2018-11-13-raspbian-stretch-lite.img ~/Desktop/os.img
```

```
> hdiutil attach os.img
/dev/disk2 (disk image):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        +1.9 GB     disk2
   1:             Windows_FAT_32 boot                    46.0 MB    disk2s1
   2:                      Linux                         1.8 GB     disk2s2                      
>
```

Now we can write to ``/Volumes/boot``.  Let's ``cd`` there first.

We copy over [``wpa_supplicant.conf``](../named_files/wpa_supplicant.conf) as discussed previously and make an empty file by ``touch ssh``.

(Actually, I already modified this copy).

Don't forget to detach.

```
> hdiutil detach /dev/disk2
"disk2" ejected.
```

If it's busy, just quit and relaunch Terminal and try again.

#### Copy to the drive

Now plug in the USB drive, erase and format it.  Then

```
> diskutil list
/dev/disk2 (external, physical):
> diskutil unmountDisk /dev/disk2
Unmount of all volumes on disk2 was successful
> sudo dd bs=1m if=os.img of=/dev/rdisk2 conv=sync
Password:
1780+0 records in
1780+0 records out
1866465280 bytes transferred in 46.334747 secs (40282194 bytes/sec)
> diskutil eject /dev/disk2
Disk /dev/disk2 ejected
>
```

#### On the Pi

Boot the Pi from the USB drive.  

From the Mac, remove 10.0.1.7 from ``known_hosts`` and then ssh in to the Pi by password login.  

From a directory containing [``sshd_config``](../code/sshd_config) on the Mac do:

```
>  
pi@10.0.1.7's password: 
sshd_config           100% 3294   456.8KB/s   00:00    
> 
```

Now on the Pi do

```
pi@raspberrypi:~ $ sudo cp sshd_config /etc/ssh
pi@raspberrypi:~ $ cat /etc/ssh/sshd_config | grep "Pubkey"
PubkeyAuthentication yes
```

Looks good.  To provide my public key I could do a direct copy but this also should work.  On the Mac

```
> ssh-copy-id -i ~/.ssh/id_rsa.pub pi@10.0.1.7
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/telliott_admin/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
pi@10.0.1.7's password: 

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'pi@10.0.1.7'"
and check to make sure that only the key(s) you wanted were added.

>
```

check the keys

```
pi@raspberrypi:~ $ cat ~/.ssh/authorized_keys 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDd1h5QmhPRT7BKEbOtQW4MLxqpEqceHny20Iy3sUQoMCn0ubN6xDrzenh116HuYYJbbZHRPNochXbbo/Fs5m2+h7fXaPdUP7N+x6EIcU8vqS8QI22lM6okFApwBIwtsoChcLfUCs+7/PWE5gVp/n2V/7dgU1KtXhKaY9htaaMnmjzWBnOb750f/SsX36rkouW+vWGLpV9EwJWlRJKkXHQY6KpCWNfZDZgBWfw4xpz5U96lWzKcxyl+8luUL4sHWzlNE0aW9ICyDbGcbIgeXQKMAF07xnbM++Ro/PugrwkctgzrH+OISEcd/AgEREl8dl1VoMwfoQElQeHXP/nT4kPB telliott999@gmail.com
```

Try logging out and back in by ssh.  

The message is annoying

```
> ssh pi@10.0.1.7
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Nov 13 14:02:54 2018 from 10.0.1.4
pi@raspberrypi:~ $ scp pi@10.0.1.7:/etc/motd motd
```

On the Pi

```
pi@raspberrypi:~/.ssh $ ls
authorized_keys  known_hosts
pi@raspberrypi:~/.ssh $ rm known_hosts 
```

On the Mac

```
> te motd
> scp motd pi@10.0.1.7:~
motd                  100%   17     2.2KB/s   00:00    
>
```

``te`` is an alias to open that file with TextEdit.  Copy the file on the Pi to the right place

```
pi@raspberrypi:~ $ sudo cp motd /etc/motd
```

Try the ssh login again

```
> ssh pi@10.0.1.7
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

Peace and love.
Last login: Fri Feb 22 16:44:34 2019 from 10.0.1.4
pi@raspberrypi:
```

```
pi@raspberrypi: sudo shutdown now
```

#### Try it again

Boot the Pi from the USB drive.  From the Mac

```
> ssh pi@10.0.1.7
Last login: Fri Feb 22 16:51:12 2019 from 10.0.1.4
pi@raspberrypi:
```

#### Save the modified OS

Shut down the Pi and transfer the USB drive to the Mac.

```
> sudo dd bs=1m count=2000 if=/dev/rdisk2 of=~/Desktop/backup-mod.img conv=sync
Password:
2000+0 records in
2000+0 records out
2097152000 bytes transferred in 15.232164 secs (137679191
>
```
and

```
> gzip backup-mod.img
> 
```

Save a copy and then

```
> gunzip backup.img.gz
>
```

#### Test the modified OS

Follow the steps above.  Plug in and erase a USB drive and then

```
> diskutil list
> diskutil unmountDisk /dev/disk2
> sudo dd bs=1m if=backup-mod.img of=/dev/rdisk2 conv=sync
> diskutil eject /dev/disk2
> 
```

I notice that gunzip did *not* remove the extra (empty?) space at the end of the image file.  That's an issue for another time.

Boot the Pi with the USB drive and then on the Mac:

```
> ssh pi@10.0.1.7
Last login: Fri Feb 22 13:33:07 2019
pi@raspberrypi:~ $
```

On the Pi we see:

```
..
Peace and love
pi@raspberry:~ $
```

I like it.