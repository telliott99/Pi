#### Setting locale

It's [easy enough](../files/1.md) when the Desktop is there.

When it's not, one solution is the command line (from the console, not ssh):

```
$ sudo raspi-config
```

#### Navigating raspi-config

Comes up with 9 options in a "pseudo-window" where you navigate

- a list of options, move with up/down/right arrows
- ``TAB`` from list to ``<Select>`` to ``<Finish>``
- ``RET`` or Enter to accept a choice 

4 Localisation Options

- ``I1 Change Locale``
- ``I2 Change Timezone``
- ``I3 Change Keyboard Layout``
- ``I4 Change WiFi Country``

#### Setting locale

``I1`` Locale

``en_US.UTF-8 UTF-8``

There is a pre-existing mark ``*`` next to ``en_GB``.  There is no indication about how to mark and unmark.

This (literally) required google to figure out.  

The [answer](http://robertawood.com/raspberry-pi/raspberry-pi-initial-setup-headless-no-monitor-or-keyboard-needed/raspi-config/) is:  ``SPACE``!

Also changed:

- Timezone
- Keyboard (Apple), Layout (Other > US, Language > __)
- WiFi Country (no need, it's already set)

