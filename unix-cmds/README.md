Preliminary note:  it's unconventional, but I am not showing the prompt that is on the Terminal after a command executes.  Just assume at the end of every listing that there is a blank line:

```
>
```
#### Basics (you know these)

- cd
- cp
- ``.`` and ``..``[syntax](dot-syntax.md)
- ls
- [ln](ln.md)
- [man](man.md)
- mkdir
- mv
- pwd
- [touch](touch.md)
- [wc](wc.md)
- whomami

#### Top of the useful list

- [find](find.md) --- and see [here](https://github.com/telliott99/MyUnix/blob/master/unix/find.rst) [more todo]
- [find + grep](find+grep.md) [todo]
- [grep](grep.md) --- and see [here](https://github.com/telliott99/MyUnix/blob/master/unix/grep.rst)
- [grep OR](grep-or.md) (x | y)
- [pipes & redirection](pipe.md)
- [sudo](sudo.md)
- [xargs](xargs.md) --- and see [here](https://github.com/telliott99/MyUnix/blob/master/unix/xargs.rst)


#### Standard Unix commands

- [alias](alias.md)
- [awk](awk.md)
- [control characters](ctl.md)
- curl --- and see [here](https://github.com/telliott99/MyUnix/blob/master/unix/curl.rst)
- [cut](cut.md)
- [diff] --- todo
- [EOF](eof.md) trick
- head, tail
- [hexdump](hexdump.md) --- and see [here](https://github.com/telliott99/MyUnix/blob/master/unix/hexdump.rst)
- [kill](kill.md)
- [ps](ps.md) --- process
- [scp]
- [sed](sed.md)
- [sort](sort.md)
- [tar and zip] (tar-zip.md)
- [tr](tr.md) --- translate
- [tree](tree.md)
- whiptail

[MyUnix](https://github.com/telliott99/MyUnix)

#### Selected additional commands

- [bgrep](bgrep.md) --- binary grep
- [pv](pv.md) --- progress viewer
- [truncate](truncate.md)

#### disk manipulation

- [mount](mount.md) and unmount
- [dd](dd.md)
- [fdisk]
- [parted](../linux/parted.md)
- [Resource busy error](resource-busy.md)
- [stat] ``-f %z <filename>``:  file size (bytes)
- [getting info](show-info.md) ``df``, ``lsblk``, ``fdisk``, etc.

#### Mac disk manipulation

- [diskutil](diskutil.md)
- [hdiutil](hdiutil.md)

#### Network

- [arp](arp.md)
- ifconfig --- see below
- [netcat]
- [nmap]

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