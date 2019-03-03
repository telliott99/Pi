#### Single file script

The previous version [here] used a fairly complicated approach:  constructing a ``tar.gz`` archive, copying it to the Pi, unpacking it, and then running commands.  I ran into trouble with time-stamps, possibly because the Pi's clock hadn't been set properly.

Version 2 is a single file:  [``do_pubkey``](do_pubkey).  

[Note: the restore in case of failure is not tested yet!]

Other scripted setup yet to do:

- modifying the Mac's authorized hosts file
- keyboard and locale, language, etc.


