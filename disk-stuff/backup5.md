#### SD card boot blues

I have an image, ``backup-mod.img``, which, when copied to a USB drive, works to boot the Pi and it behaves as expected.  

But when copied to an SD card, it doesn't work correctly.  Pretty strange!

``raspi-conf`` indicates that neither the Locale nor WiFi is set up.  But WiFi does run.

So only some of the ``wpa_supplicant.conf`` stuff is not being executed from the SD card, but is from USB!  

#### Does the WiFi work?  

Modify the original downloaded image (renamed)

```
> hdiutil attach os.img
> touch /Volumes/boot/ssh
> cp wpa_supplicant.conf /Volumes/boot/wpa_supplicant.conf
> hdiutil detach /dev/disk3
```

Erase the SD card and get a new Terminal window and do

```
sudo diskutil unmountDisk /dev/disk2
sudo dd bs=1m if=os.img of=/dev/rdisk2 conv=sync
diskutil eject /dev/disk2
```

Plug it into the Pi.

ssh with password logon works.  

Clean the host key with [``kh``](../unix-cmds/known_hosts.md)

#### To do:  fix localization

The localization is still bad, however.  Try entering ``~`` on the Pi's keyboard.

