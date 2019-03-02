Raspbian Stretch is the Pi OS with a desktop but not the full load of extra software.

#### Quick summary of install

On the Mac:

One-time setup:  download the image from [here](https://www.raspberrypi.org/downloads/raspbian/).  

I put it in ``~/Downloads-saved/Stretch``.

```
cd ~/Downloads-saved/Stretch
unzip 2018-11-13-raspbian-stretch.zip
```

To install the image, insert a USB drive or SD card (in a USB card reader) and do:

```
diskutil list
```

we learn that it is e.g. ``/dev/disk2``.  Reformat as FAT32:

```
diskutil eraseDisk MS-DOS SD MBR /dev/rdisk2
diskutil unmountDisk /dev/rdisk2
```

From the directory containing ``2018-11-13-raspbian-stretch.img`` do

```
sudo dd bs=1m if=2018-11-13-raspbian-stretch.img of=/dev/rdisk2 conv=sync
3248+0 records in
3248+0 records out
3405774848 bytes transferred in 108.584718 secs (31365140 bytes/sec)
```

The ``r`` in ``rdisk`` is important.  After 108 seconds or so...

```
sudo diskutil eject /dev/disk2
```

Remove the SD card from the Pi and insert the USB drive.  Power up.  It works, and boots to the desktop.
