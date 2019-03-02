#### hostname works

[link](https://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/)

All that is necessary is to use the right domain (.local).  ``ping raspberrypi.local`` works as does

```
> ssh pi@raspberrypi.local
The authenticity of host 'raspberrypi.local (fe80::4985:8f96:e28c:8723%en0)' can't be established.
ECDSA key fingerprint is SHA256:TUhSRzj3662Nx4kv61xoxD7AQrNrPiD6n4VzDiUfIH8.
..
```

So the Pi comes with mDNS like Bonjour or avahi-daemon already installed!

```
pi@raspberrypi:~ $ apt list --installed | grep "avahi"

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

avahi-daemon/stable,now 0.6.32-2 armhf [installed]
libavahi-common-data/stable,now 0.6.32-2 armhf [installed,automatic]
libavahi-common3/stable,now 0.6.32-2 armhf [installed,automatic]
libavahi-core7/stable,now 0.6.32-2 armhf [installed,automatic]
```

And it does have avahi.  

All that was needed is to say ``raspberrypi.local`` rather than ``raspberrypi``.

And if you find the right [ref](https://www.raspberrypi.org/forums/viewtopic.php?t=18207), that's what it says!

```
pi@raspberrypi:~ $ cat /etc/hostname
raspberrypi
```

Change that?
Nah...

Just make an alias

```
alias spi="ssh pi@raspberrypi.local"
```

in my ``~/.bash_profile`` for ssh into pi.

