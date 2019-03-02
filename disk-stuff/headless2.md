Last time we wrote .img to the USB drive and then booted the Pi with it, before doing shutdown and going back to the Mac to modify the drive.

I <i>could</i> burn the .img to the USB drive, and then change it.  I could even change from Linux on the Pi like [this](https://learnaddict.com/2016/02/23/modifying-a-raspberry-pi-raspbian-image-on-linux/)

However, I just want to try modifying the unzipped version as it is on the Mac first.

#### headless Lite from Mac

I make a copy of the .img file on the Desktop and ``attach`` it.

```
> cd ~/Desktop
> hdiutil attach 2018-11-13-raspbian-stretch-lite.img
/dev/disk2          	FDisk_partition_scheme         
/dev/disk2s1        	Windows_FAT_32                 /Volumes/boot
/dev/disk2s2        	Linux                          
> 
```

Then edit ``/Volumes/boot`` exactly as before

```
> touch /Volumes/boot/ssh
> cp wpa_supplicant.conf /Volumes/boot
> 
```

Now

```
> hdiutil detach disk2
"disk2" ejected.
>
```

*Not* ``2018-11-13-raspbian-stretch-lite.img``!

That was easy!

Now burn it to the USB drive exactly [as before](headless1.md) and it should work with

```
ssh pi@10.0.1.7
```

Or, I suppose we could just modify the .img file on the USB drive.
