### Project

I decided to explore the [Raspberry Pi](https://www.raspberrypi.org).  So, recently I [ordered](named_files/orders.md) a few things from Amazon.

These pages are not organized or succinct enough to be a tutorial, but they are more like the log from an expedition.  I've written to remind me of where I've been and what I did there.

#### Raspberry Pi

Most people start with the Pi to do electronics or robotics projects or possibly even to learn Python.  

My main interest at the moment is that the Pi is a very inexpensive computer running Linux.  And the Pi seems much more convenient to work with than a virtual machine like [this one](https://github.com/telliott99/Ubuntu) I worked with before.

But the Python thing is also *very* attractive.

#### Docs

The official Pi docs are [here](https://www.raspberrypi.org/documentation/).

<hr>

#### Day 0:  getting to boot

- [file systems](named_files/file-systems.md) or why FAT32
- [SD card](named_files/sd.md) basics
- An SD card [reader](named_files/sd-reader.md)
- A (cheap) [monitor](files/16.md)
- [memory](named_files/memory.md) on the Pi
- [initial setup](files/0.md) to power-up

#### NOOBS

If you haven't worked with Linux much, you should look at NOOBS.  It allows you to choose a version if the Raspbian Stretch OS and then it basically sets itself up.

The micro SD card I bought ([here](https://www.amazon.com/gp/product/B01H5ZNOYG/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)) came with NOOBS installed, and it was pre-expanded so that it came to the Desktop about 10 seconds after I turned it on.  That's a great place to start. 

If you'd rather roll your own (or you accidentally wrote over your NOOBS like I did)

- [reformat](files/22.md) a USB drive or SD card (w/ reader)
- download NOOBS, and copy files to the [drive](files/4.md)
- [boot the Pi](named_files/boot-the-pi.md) (insert the card and power up)

Depending on the exact version of NOOBS, you will prompted early on for your WiFi network name and password.

You should also set the Locale, language and keyboard when given the chance (Language: US English, Keyboard: US).

Stretch Full takes about 10 min to boot.

### Stretch and Stretch Lite

By now (two weeks), I've installed the OS maybe a hundred or so times.  

In many ways the easy install is the whole point.  Experimentation is cheap.  If you mess up completely, you can always start over again with a clean OS image in about 5 minutes.

- The Raspbian software repository is [here](https://raspbian.org/RaspbianRepository)
- All previous versions of Stretch are [here](http://downloads.raspberrypi.org/raspbian/images/)
- Stretch-Lite is [here](http://downloads.raspberrypi.org/raspbian_lite/images/)

If you have a dedicated monitor and want a Desktop, it's probably just as easy to use the GUI tools to do the setup.  If you don't have a Desktop (you're using Lite), or you find yourself installing repeatedly, there ways to automate much of the process.  

#### Stretch + Desktop configuration

Copying an image is covered below.  Here we have booted the Pi with an SD card or USB drive having Stretch Full.

- set up [WiFi](files/1.md) from the Desktop
- start the [ssh](files/1a.md) server
- [remote desktop](files/2.md) by ``tightvncserver``
- [scp](files/6.md) (secure copy) and copy-paste

#### Public key authentication

Initial ssh gives login via password.  We want to use a Public/Private(Secret) key pair:

- [Pubkey Authorization](files/3.md) for ssh
- [update](files/17.md) ssh host
- use [hostname](named_files/hostname.md) instead of ip address

#### Notes

- I am monitoring the Pi by ssh and remote Desktop over the WiFi network.  I find it convenient to do some work on my Mac.  A second computer isn't necessary, and **you can certainly use a PC instead**, but I don't use or even have Windows, so YMMV.

We're using two computers here.  Lines starting

- ``> `` are on the Mac
- ``$ `` or ``pi@raspberrypi:~ $`` are on the PI

- I've assumed you know something about the command line.  You can follow along by cut-and-paste, but I haven't explained the most basic commands like ``cd`` and ``ls`` and ``cp`` and so forth.

#### Stretch install 

A download and install of Stretch + Desktop from a .img file:

- [quickstart](disk-stuff/stretch-quick.md)
- [full version](disk-stuff/stretch.md)

#### Stretch-Lite with no desktop

- [quickstart](disk-stuff/stretch-lite-quick.md)
- [setting up](disk-stuff/headless1.md) headless Lite
- [variation](disk-stuff/headless2.md), modify the disk image first
- cool [script](disk-stuff/script-setup.md) for auto Pubkey Auth setup
- [modifying](files/17.md) ``known_hosts`` on the Mac
- [set locale](named_files/locale.md) from the command line
- [keyboard](named_files/keyboard.md) issues [more to do]
- save the modified OS (see backups, below)

#### Unix stuff

- [my quick intro](unix-cmds/main.md) to selected Unix commands
- [link](https://en.wikibooks.org/wiki/Guide_to_Unix/Commands) to wiki guide to Unix commands
- simple example of [C compilation](files/7.md)
- [upgrading to Python 3.7](files/8.md) plus matplotlib
- [``$PATH``](files/5.md), a shaggy dog story
- [.bash_profile](files/5a.md)
- [link](http://linuxcommand.org/index.php) to a guide to learning the command line

[Here](http://www.ee.surrey.ac.uk/Teaching/Unix/) is a good introduction to Unix.

#### Python

Pi stands for Python, [here](named_files/python.md) are a few cool examples of mine and links to many other things I've written about Python.

[Here](https://docs.python.org/3/tutorial/) is the official Python tutorial.  And [here](https://github.com/telliott99/PyBioinformatics) is a book that I wrote about using Python for Bioinformatics.

#### Web servers and frameworks

- [apache, nginx, flask](servers/README.md)

#### Saving backups

- [quickref](disk-stuff/quickref.md)
- [write](disk-stuff/backup4.md) image to SD card (WiFi and ssh active)

Several days work on disk images and backups, copying, etc. are chronicled [here](disk-stuff/README.md).  

One can save a modified system as a disk image, and re-install it on a USB drive or SD card and have it work.m
At this point, I copied over a Lite image with WiFi and SSH on, turned on PubKey Auth, went through the ``raspi-config`` dance, installed apache2 and nginx and tested them.  I want to save it back to the Mac as a .img file.

I need to know the right size.  ``df -h`` says we're using only 1.1 GB for /dev/root.

Try 1.5 GB.



#### Text, typesetting and more

- LaTeX --- not done yet
- Sphinx --- not done yet

#### Current stuff

- Growing my [Linux Fu](linux/main.md)

#### A bit more about SSH

- the [math](https://github.com/telliott99/CryptoQuickies/blob/master/public-key_math.md) of Public Key cryptography
- [generating](files/18.md) a Public-private key pair
- a (slightly hokey) encryption [example](files/19.md)
- [ssh](files/17a.md) passphrase macOS quirk

#### General info about passwords

- my notes on [password complexity](named_files/pw_complexity.md)
- [generating](named_files/pw_util.md) passwords from the command line

#### Ideas for future projects

- [433 MHz receiver](https://www.princetronics.com/how-to-read-433-mhz-codes-w-raspberry-pi-433-mhz-receiver/) on Pi, other IOT stuff
- [LIRC](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/) --- control your TV
- GPIO [stuff](http://razzpisampler.oreilly.com/ch07.html)
- [weather station](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station)
- [touchscreen](https://www.pishop.us/product/official-raspberry-pi-7-touch-screen-display-with-10-finger-capacitive-touch/?src=raspberrypi)
- [hardcore](named_files/hardcore.md) software

<hr>

I am keeping an eye on [Atomic Pi](https://www.kickstarter.com/projects/323002773/atomic-pi-a-high-power-alternative-to-rpi/updates) --- [more](http://www.digital-loggers.com/api.html).  Order [here](https://dlidirect.com/products/atomic-pi).

Since these pages haven't been read much by others, there is a higher probability of errors or bugs than otherwise.  If you find one please let me know.

