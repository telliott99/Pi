TL;DR

- [quickref](quickref.md)

#### Making backups

I spent quite a bit of time learning how to resize a partition [on the Pi](../linux/linux-resize.md), and [on the Mac](mac-resize.md).  

It turns out this isn't necessary!  But when I did the first example here, I didn't know that yet.

- [almost all Pi](backup.md)
- [mostly Mac](backup2.md)
- [backup](backup3.md) + Pubkey Auth, USB works
- [backup](backup4.md) + Pubkey Auth, SD does not work
- WiFi + ssh [only](backup5.md), SD works
- Pubkey Auth [works on SD](quickref.md)

I [figured out](quickref.md) the trick to Pubkey Auth on SD:  the saved image must come from an SD card, it won't work if the mod was made on a USB drive.

We add two files in ``boot`` (a FAT32 partition), an empty one named ``ssh`` and [``wpa_supplicant.conf``](wpa_supplicant.conf).  With just them, the setup of WiFi and password works fine on both SD and USB.

I saw a suggestion to run an arbitrary script on Pi boot by changing ``cmdline.txt`` like [this](boot-script.md), but it didn't work for me.

So I decided to write a script that can run from the Mac with the micro SD card from above booting the Pi and do the rest of the setup over ssh.

- [detailed description](script-setup.md) of configuration script

I did this in stages, not all at once, like any programming project.

#### Notes

- [disk versus rdisk](rdisk.md)

#### older

- [headless](lite.md) boot of Stretch Lite from a USB thumb drive
- [quick reference](named_files/headless.md)
- How to [umount](files/9.md) USB drive with several partitions?
