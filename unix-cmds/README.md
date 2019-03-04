Preliminary note:  it's unconventional, but I am not showing the prompt that is on the Terminal after a command executes.  Just assume at the end of every listing that there is a blank line:

```
>
```

#### Standard Unix commands

[MyUnix](https://github.com/telliott99/MyUnix)

- [alias](alias.md)
- [arp](arp.md)
- [awk](awk.md)
- [bgrep](bgrep.md)
- [control characters](ctl.md):  ``CTL-Z``,``CTL-C``,``CTL-D``
- [cut](cut.md)
- curl --- see [here](https://github.com/telliott99/MyUnix/blob/master/unix/curl.rst)
- [cut](cut.md)
- [dd](dd.md)
- [diskutil](diskutil.md)
- [EOF](eof.md) trick
- find --- see [here](https://github.com/telliott99/MyUnix/blob/master/unix/find.rst)
- [grep](grep.md) --- [more](https://github.com/telliott99/MyUnix/blob/master/unix/grep.rst)
- head, tail
- [hdiutil](hdiutil.md)
- [hexdump](hexdump.md) --- see [here](https://github.com/telliott99/MyUnix/blob/master/unix/hexdump.rst)
- ifconfig --- see below
- kill
- [ln](ln.md)
- [man](man.md)
- [nmap]
- [parted](../linux/parted.md)
- [ps]
- [pipes & redirection](pipe.md):  ``|``, ``>``, ``<``, ``>>``
- [ps](ps.md)
- [pv](pv.md)
- [sed](sed.md)
- [sort]
- [stat] ``-f %z <filename>``:  file size (bytes)
- [sudo](sudo.md)
- [tar and zip] (tar-zip.md)
- [touch](touch.md)
- [tr](tr.md) --- translate
- [truncate](truncate.md)
- wc
- whiptail
- xargs --- see [here](https://github.com/telliott99/MyUnix/blob/master/unix/xargs.rst)

#### Selected additional Unix commands

- [bgrep](bgrep.md) --- binary grep
- [pv](pv.md) --- progress viewer
- [truncate](truncate.md)

#### disk manipulation

- [mount](mount.md) and unmount
- [dd](dd.md)
- [Resource busy error](resource-busy.md)
- [getting info](show-info.md) ``df``, ``lsblk``, ``fdisk``, etc.

#### Mac disk manipulation

- [diskutil](diskutil.md)
- [hdiutil](hdiutil.md)

Possible fix for a drive that [won't show up](borked-drive.md)

### common Pi stuff

#### ifconfig

```
pi@raspberrypi:~ $ ifconfig
..
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.1.7  netmask 255.255.255.0  broadcast 10.0.1.255
..
```

#### shutdown

```
sudo shutdown now       # default -P poweroff
sudo shutdown -r now    # -r means reboot
```

#### scp (secure copy)

```
scp pi@10.0.1.7:example.png ~
scp ~/Desktop/hashme.py pi@10.0.1.7:bin
```

#### dpkg:  list installed packages

```
dpkg --list
```