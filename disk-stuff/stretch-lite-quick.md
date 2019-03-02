Raspbian Stretch Lite is the Pi OS with no desktop.  It is designed to be run from the command line, or in "headless" mode.

#### Summary of steps

On the Mac:

One-time setup:  download the image from [here](https://www.raspberrypi.org/downloads/raspbian/).

```
cd ~/Downloads-saved/Stretch-Lite
unzip 2018-11-13-raspbian-stretch-lite.zip
```

To install the image, insert either a USB drive or SD card (in a card reader) and do:

```
diskutil list   # e.g. /dev/disk2
diskutil eraseDisk MS-DOS TE /dev/rdisk2
diskutil unmountDisk /dev/rdisk2
```

From the directory containing ``2018-11-13-raspbian-stretch-lite.img`` do

```
sudo dd bs=1m if=2018-11-13-raspbian-stretch-lite.img of=/dev/rdisk2 conv=sync
Password:
1780+0 records in
1780+0 records out
1866465280 bytes transferred in 44.873158 secs (41594248 bytes/sec)
```

After 45 seconds or so... (or 180 sec for an SD card)

```
diskutil eject /dev/disk2
```

Remove the SD card from the Pi and insert the USB drive.  Power up.  It works, and boots to the command line, asking for a login.