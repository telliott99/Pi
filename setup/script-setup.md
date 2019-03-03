TL;DR

- Put a target USB drive into the Mac
- run:  ``scripts/write`` to erase, format and copy
- Put the drive into the Pi
- Power up
- run:  ``scripts/do_all``

#### Single file scripts for setup

We want to setup the Pi for ssh using a script run on the Mac.  The Pi has been booted with Stretch Lite (WiFi+ and Password Auth for SSH+).

Erasing the disk and writing the .img file is performed by this script:

[``write``](scripts/write)

#### First version

We want to setup the Pi for ssh using a script run on the Mac.  

The first version [here](old/script-setup.md) used a fairly complicated approach:  constructing a ``tar.gz`` archive, copying it to the Pi, unpacking it, and then running commands.  

It does work but I ran into trouble with time-stamps, possibly because the Pi's clock hadn't been set properly.

#### Revised version

The script is broken into parts run by doing:  [``scripts/do_all``](scripts/do_all).  

Other scripted setup yet to do:

- keyboard and locale, language, etc.
- change default password


