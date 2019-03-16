TL;DR

I booted a copy of ``lite-wifi.img`` on the Pi (Lite with WiFi and ssh enabled through the write to ``/boot``), then did  ``sudo raspi-config`` and configured locale and keyboard by hand.  

After that, I saved a copy as ``lite-conf.img``.  The following seems to work well:

- Put a target USB drive into the Mac
- run:  ``write-lite-conf`` to erase, format and copy
- Put the drive into the Pi
- Power up
- run:  ``setup/client-script`` to do Pubkey stuff

Then run

- ``servers/do_apache2``
- ``servers/nginx``

to install apache and nginx and configure them.

I have had successes and failures saving these versions and booting with them.  I even had a failure that then turned itself into success.  Boot is quite slow because of a disk check that happens.

Maybe ``dd`` with ``rdisk`` makes errors?  The saved versions are ``lite-pub.img`` and ``lite-all.img``, but the recommended method is to use ``lite-conf.img`` and then run ``setup/client-script``.

#### Single file scripts for setup

We want to setup the Pi for ssh using a script run on the Mac.  The Pi has been booted with Stretch Lite (WiFi+ and Password Auth for SSH+).

Erasing the disk and writing the .img file is performed by this script:

[``write``](write-lite)

#### First version

We want to setup the Pi for ssh using a script run on the Mac.  

The first version [here](old/script-setup.md) used a fairly complicated approach:  constructing a ``tar.gz`` archive, copying it to the Pi, unpacking it, and then running commands.  

It does work but I ran into trouble with time-stamps, possibly because the Pi's clock hadn't been set properly.

#### Revised version

The script is broken down into parts that are run by doing:  [``scripts/do_all``](scripts/do_all).  

#### Third version

Take advantage of ``-r`` flag to ``scp`` to copy over ``tmp`` directory containing data files plus a ``server-script``.

Upper level has 2 client-side scripts.  

Copy the ``scripts`` directory to the Desktop and from the Desktop do

- ``setup/kill-previous``
- ``setup/client_script``

#### Scripting install of apache2 and nginx

Copy the ``server`` directory to the Desktop and from the Desktop do ``do_apache``, or ``do_nginx``.

[Still in progress]

#### To do

Other scripted setup yet to do:

- keyboard and locale, language, etc.
- change default password
