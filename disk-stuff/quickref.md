TL;DR

There's a standard hack ([here](https://www.raspberrypi.org/documentation/remote-access/ssh/) and [here](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)) of writing ``ssh`` (empty) and [``wpa_supplicant.conf``](wpa_supplicant.conf) to the ``/boot`` directory of a disk image.  

With those changes, when the Pi boots, WiFi and ssh are automatically on.  

But I wanted Pubkey Authorization automatically on too, so I wrote a script which automates the setup for this from the Mac, using [``sshpass``](https://gist.github.com/arunoda/7790979). 

(I just unzip ``setup-pi.tar.gz`` from this directory and run ``setup-pi/go``.  The path to my Public key is hard coded so you would have to make modifications).

Modified systems from both a USB drive and SD can be saved as disk images.  The trick is that the image for an SD card must have been previously modified on such a card.  Another important thing is that when writing from USB drive or SD card to an image file, to pass the ``count`` option to ``dd`` so the amount of data written is limited.

#### Quickref

[Download](https://www.raspberrypi.org/downloads/raspbian/) the zipped image for Raspbian Stretch-Lite. 

Check the hash and save it.  

Copy to the Desktop in case we mess things up. Unzip and rename it.

```
tar -zxvf 2018-11-13-raspbian-stretch-lite.zip
mv 2018-11-13-raspbian-stretch-lite.img lite.img
rm 2018-11-13-raspbian-stretch-lite.zip
```

#### Test the unmodified image on USB

Insert a USB drive and check the disk number

```
> diskutil list | grep "external"
/dev/disk2 (external, physical):
```

Erase and partition

```
diskutil eraseDisk MS-DOS USB MBR /dev/disk2
```

Write the image to the USB drive

```
diskutil unmountDisk /dev/disk2
sudo dd bs=1m if=lite.img of=/dev/rdisk2 conv=sync
diskutil eject /dev/disk2
```

Boot the Pi from USB and check the command line on the monitor.  It comes up to the login.  Login with password and ``sudo shutdown now``.

#### Test the image with WiFi and ssh enabled on USB

Make a copy of ``lite.img`` on the Mac.

```
cp lite.img lite-wifi.img
```

then write the changes

```
hdiutil attach lite-wifi.img
diskutil list | grep "disk image"
cd /Volumes/boot
```

```
touch ssh
cp ~/Desktop/wpa_supplicant.conf .
cat wpa_supplicant.conf
cd ~/Desktop
hdiutil detach /dev/disk2
```

Insert a USB drive 

```
diskutil list | grep "external"
```
Use Disk Utility to erase it and format as FAT32 w/MBR or do it from the command line:

- file-system name partition disk:

```
diskutil eraseDisk MS-DOS USB MBR /dev/disk2
```

Then

```
diskutil unmountDisk /dev/disk2
sudo dd bs=1m if=lite-wifi.img of=/dev/rdisk2 conv=sync
diskutil eject /dev/disk2
```

Test it by booting the Pi with only the USB drive (no SD card) and with the monitor on.  Login and do 

```
$ ifconfig
..
wlan0 .. 10.0.1.7
```

Also check by ssh from the Mac.  It should not be necessary to modify ``known_hosts``--- no Pubkey Authorization yet.

```
ssh pi@10.0.1.7
```

Goes to password login.  ``sudo shutdown now``

#### Pubkey Auth

Set up the Pi how you like.  I run my [setup script](script-setup.md) (by ssh from the Mac) which will setup Pubkey Authorization and copy my public key over.

Restart the Pi:

```
sudo shutdown -r now
```

Test ``ssh`` from the Mac.  No password needed.

Power down the Pi, and eject the USB drive.

#### Save/test the second modified image on USB

Insert the USB drive into the Mac.

```
diskutil list | grep "external"
diskutil unmountDisk /dev/disk2
sudo dd bs=1m count=2500 if=/dev/rdisk2 of=~/lite-pub.img conv=sync
```

Don't forget the ``count``!!

and

```
diskutil eject /dev/disk2
```

Remove and reinsert the USB drive.  Repeat steps from above except use ``Lite-Pubkey.img`` as the infile.

```
> ssh pi@10.0.1.7
Last login: Mon Feb 25 16:04:42 2019
pi@raspberrypi:~ $
```

You will need to modify ``known_hosts`` first by doing ``kh``, see [here](../unix-cmds/alias.md).

Looks great.

#### Test SD card

Next up, try the SD card.  (Use ``SD`` as the name).  Do the same steps as above starting with each of the saved .img files.

- lite.img works fine
- lite-wifi.img
- lite-Pubkey.img

Tested the first two.  Saving that card for the moment.  Should get some new 8GB cards today.

I expect the third one to fail, that's what happened before.

Test lite-Pubkey.img on SD:  kernel panic

Retest the same image on USB:  works fine

#### SD success

- load lite-wifi on an SD card
- run setup script
- try saving that and re-loading it on SD

It works.  So what doesn't work is to boot and modify a USB drive with the OS, then save it as a disk image, and then load that onto an SD card.

If both steps are done on an SD it's fine.