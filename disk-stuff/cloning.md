####  Cloning a startup disk 

We've been through downloading .img files with the OS and then copying them to a USB drive to boot the Pi.  We also saw how to write to the image.

What we didn't do is to modify the files to have only ssh by Pubkey Authentication, and to have the users Public key.

The easiest way to do that is to use the USB disk to boot the Pi, and make the changes.

Once we have our boot disk set up perfectly, we'd like to save a copy as a .img or .dmg file on the Mac to facilitate making copies and restoring if it gets corrupted.

#### cloning

Let's first try to make a basic clone, following [this](https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911).

The Pi resizes the EXT4 partition on startup.  The code is on the EXT4 side in ``/usr/bin/raspi-config`` according to [this](https://www.raspberrypi.org/forums/viewtopic.php?t=174434).  But it actually calls something else, ``/sbin/resize2fs``.

In any case, the point is that the Pi resizes automatically to the full size of the drive

And unfortunately, when ``dd`` is called with the USB drive as the infile and some target on the Mac's Desktop, it wants to copy the whole 32 GB drive.

#### resizing partitions

I figured out how to [resize partitions on the Mac](mac-resize.md).  But the Pi always resizes to the size of the disk, not the original FAT32 partition.

I also figured out how to [resize partitions on Linux](linux-resize.md).  But even in that case, ``dd`` wants to copy the whole drive.

One solution might be to use small drives or SD cards.  I can get 8 GB cards and may try that soon.

I had example where the guy did:



