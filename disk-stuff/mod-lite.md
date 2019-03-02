TL;DR 

It is pretty easy to modify the .img file for Stretch-Lite so that it can boot on the Pi in headless mode, with ssh on and WiFi set up.

#### headless Lite from Mac

I <i>could</i> burn the .img to the USB drive, and then change it.  I could even change from Linux on the Pi like [this](https://learnaddict.com/2016/02/23/modifying-a-raspberry-pi-raspbian-image-on-linux/)

However, I just want to try modifying the unzipped version as it is on the Mac first.

So first we ``attach`` it.

```
> cd Stretch-Lite
> hdiutil attach 2018-11-13-raspbian-stretch-lite.img
/dev/disk2          	FDisk_partition_scheme         	
/dev/disk2s1        	Windows_FAT_32                 	/Volumes/boot
/dev/disk2s2        	Linux                          	
> 
```

Then just edit ``/Volumes/boot``

```
> cd /Volumes/boot
> touch ssh
> touch /Volumes/boot/wpa_supplicant.conf
> te /Volumes/boot/wpa_supplicant.conf
> 
```

``te`` is an alias to open the file with TextEdit.  Put this in ``wpa_supplicant.conf``

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="Apple Network e7d46b"
    psk="<pw>"
    key_mgmt=WPA-PSK
}
```
Substitute my password for ``<pw>``.

Then ``detach`` it

```
> hdiutil detach disk2
hdiutil: couldn't unmount "disk2" - Resource busy
> cd
> hdiutil detach disk2
"disk2" ejected.
>
```

That was easy!

Now burn it to the USB drive exactly as before.  Erase and reformat as FAT32 first.  

Then check with ``diskutil list``, it is disk 2 as before.

```
> cd Desktop/Stretch_Lite
```

And oh so carefully..

```
> sudo dd bs=1m if=2018-11-13-raspbian-stretch-lite.img of=/dev/rdisk2 conv=sync
..
> sudo diskutil eject /dev/rdisk2
Disk /dev/rdisk2 ejected
>
```

Now test.  

Attach the monitor to the Pi just to watch the progress...

Login on the Pi and then ``sudo ifconfig`` and it comes back with ``wlan0`` which is configured and has the expected ip address ``10.0.1.7``.

On the Mac

```
> ssh pi@10.0.1.7
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:nhBsC4GC+LTolbCj22NIHDrtyYf8acZvHPSFwV3jWPI.
Please contact your system administrator.
```
more 

```
Add correct host key in /Users/telliott_admin/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/telliott_admin/.ssh/known_hosts:13
ECDSA host key for 10.0.1.7 has changed and you have requested strict checking.
Host key verification failed.
>
```

So what is happening is that ssh works, we are talking to the Pi.  However, the Pi's key fingerprint sent by the ssh server is

```
SHA256:nhBsC4GC+LTolbCj22NIHDrtyYf8acZvHPSFwV3jWPI
```

which doesn't match what we have (because we were using a different OS install before.

There are ways to get past this e.g. [here](https://askubuntu.com/questions/87449/how-to-disable-strict-host-key-checking-in-ssh), but the easiest is to edit ``~/.ssh/known_hosts`` on the Mac to remove the key for 10.0.1.7 at the end of the file.

``open -a TextEdit ~/.ssh/known_hosts``

Maybe we can have two different keys for the same server?


