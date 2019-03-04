I got the source of ``raspi-config`` from [here](https://github.com/asb/raspi-config), but it's pretty complicated.  It calls other things.  

One thing recommended on the web is ``sudo dpkg-reconfigure locales`` but this just puts up the pseudo-GUI we're trying to avoid.

However, eventually I came across [this](https://raspberrypi.stackexchange.com/questions/28907/how-could-one-automate-the-raspbian-raspi-config-setup).

It turns out that ``raspi-config`` has a non-interactive mode, as in

```
sudo raspi-config nonint do_change_locale
```

which gives

```
sudo: unable to resolve host raspberrypi
```

The [solution](https://raspberrypi.stackexchange.com/questions/64548/pi3-unable-to-resolve-host-message) :  

edit ``/etc/hosts`` to add:

```
127.0.1.1       raspberrypi
```

So then

```
$ locale=en_US.UTF-8
$ sudo raspi-config nonint do_change_locale $locale
Generating locales (this might take a while)...
  en_US.UTF-8... done
Generation complete.
```






