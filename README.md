### Project

Recently, I decided to explore the [Raspberry Pi](https://www.raspberrypi.org).  

So I [ordered](named_files/orders.md) a few things from Amazon.

These pages are not organized or succinct enough to be a tutorial on the Pi, they are more like the log from an expedition.  I've written them to remind me of where I've gone and what I did while I was there.

#### Raspberry Pi

Pi stands for Python, which is my favorite programming language and by far the best choice for a first language.

Most people start with the Pi to do electronics or robotics projects or possibly even to learn Python.  

My main interest has been that the Pi is a very inexpensive computer running Linux.  And it seems much more convenient to work with than a virtual machine like [this one](https://github.com/telliott99/Ubuntu) I worked with before.

But the Python thing is also *very* attractive.

#### Docs

The official Pi docs are [here](https://www.raspberrypi.org/documentation/).

#### Note

- Some knowledge about the command line is assumed.  You can follow along by cut-and-paste, but I haven't explained the most basic commands like ``cd`` and ``ls`` and ``cp`` and so forth.

Suggestions for learning more about Unix and Linux are below.

<hr>

#### Day 0:  getting to boot

- [file systems](named_files/file-systems.md) or why FAT32
- [SD card](named_files/sd.md) basics
- An SD card [reader](named_files/sd-reader.md)
- A (cheap) [monitor](files/16.md)
- [memory](named_files/memory.md) on the Pi
- [initial setup](files/0.md) to power-up

#### NOOBS

If you haven't worked with Linux much, you should look at NOOBS.  It allows you to choose a version of the Raspbian OS (the current release is **Stretch**), and then it basically sets itself up.

The micro SD card I bought ([here](https://www.amazon.com/gp/product/B01H5ZNOYG/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)) came with NOOBS installed, and it was pre-expanded so that it came to the Desktop about 10 seconds after I turned it on.  That's a great place to start. 

<hr>

#### Note

- I find it convenient to monitor the Pi by **ssh (secure shell)**.

I'm using a Mac as the client computer, from which I ssh *into* the Pi as a server.  Occasionally, I use a remote Desktop over the WiFi network.

- **You can use a PC as the client** instead.  I don't have Windows, so YMMV.

Since we have two computers here, it helps to have different prompts on the command line.  

- Lines starting ``$ `` or ``pi@raspberrypi:~ $`` are on the PI.

- Lines starting ``> `` are on the Mac.

#### Download NOOBS

If you'd rather roll your own (or you accidentally wrote over your NOOBS like I did)

- [reformat](files/22.md) a USB drive or SD card (w/ a reader)
- download NOOBS, and copy files to the [drive](files/4.md)
- [boot the Pi](named_files/boot-the-pi.md) (insert the card and power up)

Depending on the exact version of NOOBS, you will prompted early on for your WiFi network name and password.

You should also set the Locale, language and keyboard when given the chance (For me, Language: US English, Keyboard: US).

Stretch Full takes about 10 min to boot.

### Stretch and Stretch Lite

By now (two weeks), I've installed the OS maybe a hundred or so times.  

In many ways the easy install is the whole point.  Experimentation is cheap.  If I mess up completely, I can always start over again with a clean OS image in under 5 minutes.

- The Raspbian software repository is [here](https://raspbian.org/RaspbianRepository)
- All previous versions of Stretch are [here](http://downloads.raspberrypi.org/raspbian/images/)
- Stretch-Lite is [here](http://downloads.raspberrypi.org/raspbian_lite/images/)

If you have a dedicated monitor and want a Desktop, it's probably just as easy to use the GUI tools to do the setup.  If you don't have a Desktop (you're using Lite), or you find yourself installing repeatedly, there are ways to automate much of the process, see below.  

#### Stretch + Desktop configuration

Copying an image is also covered below.  Here we have booted the Pi from an SD card or USB drive with Stretch Full.

- set up [WiFi](files/1.md) from the Desktop
- start the [ssh](files/1a.md) server
- [remote desktop](files/2.md) by ``tightvncserver``
- [scp](files/6.md) (secure copy) and copy-paste

<hr>

#### Public key authentication

Initial ssh gives login via password.  We want to use a Public/Private(Secret) key pair:

- [Pubkey Authorization](files/3.md) for ssh
- [update](files/17.md) ssh host
- use [hostname](named_files/hostname.md) instead of ip address
- correcting issues w/ ``known_hosts`` --- see below

#### Stretch install 

A download and install of Stretch + Desktop from a .img file:

- [quickstart](disk-stuff/stretch-quick.md)
- [full version](disk-stuff/stretch.md)

#### Stretch-Lite with no desktop

- [quickstart](disk-stuff/stretch-lite-quick.md)
- [setting up](disk-stuff/headless1.md) headless Lite
- [variation](disk-stuff/headless2.md), modify the disk image first

#### raspi-config

There are a number of configuration details that must be accomplished *after* first boot (or at least, I don't know how to do them before).

``raspi-config`` is the tool to set locale, keyboard, and more, on the Pi.  It has a bit of a learning curve..

I [spent](config/README.md) [notes] a lot of time trying to figure out how to do the equivalent actions from the command line, but failed.

#### Scripting setup

- [scripts](setup/README.md) for auto Pubkey Auth setup
- [installing](auto-setup/READEME.md) or just look at the files in ``auto-setup/setup``.

Short version:  I wrote

- a script to write the OS image to a USB drive
- one to configure the Pi as far as Pubkey Auth ssh [here](setup/README.md)

My approach has been to boot a version of Lite with WiFi and then do the ``raspi-config`` stuff by hand and save the image as ``lite-config.img``.

The modified OS was saved as described in **Saving backups**, below.

Then I boot with that and do the scripting as documented above.

#### ``known_hosts``

- [Issues](files/17.md) with ``known_hosts`` on the Mac

I wrote a Python script to remove previous keys associated with the Pi from ``~/.ssh/known_hosts`` on the Mac.  It's in ``~/bin``, which is on my path, and can be invoked by doing

```
kill_previous
```

A copy of the script file is [here](auto-setup/setup/kill_previous).

#### Saving backups

- [quickref](disk-stuff/quickref.md)
- [write](disk-stuff/backup4.md) image to SD card (WiFi and ssh active)

Several days work on disk images and backups, copying, etc. are chronicled [here](disk-stuff/README.md).  

One can save a modified system as a disk image, and re-install it on a USB drive or SD card and have it work.
At this point, I copied over a Lite image with WiFi and SSH on, turned on PubKey Auth, went through the ``raspi-config`` dance, installed apache2 and nginx and tested them.  I want to save it back to the Mac as a .img file.

I need to know the right size.  ``df -h`` says we're using only 1.1 GB for /dev/root.  1.5 GB works fine.

This works, but it's flaky.  I recommend the sequence described above:

- modify an image of Lite to turn on WiFi and ssh
- boot the Pi with that copied to a USB drive
- run ``sudo raspi-config``
- save that image and copy it when needed 
- boot the Pi with that
- setup Pubkey Authentication as in ``auto-setup/setup``
- install software like webservers as in ``auto-setup/servers``

#### Web servers and frameworks

See [here](servers/README.md) for how to set up two servers:

- apache
- nginx

A Python web framework called [Flask](http://flask.pocoo.org) is introduced in some detail:

- [flask](flask/README.md)


<hr>

#### Unix stuff

- [my quick intro](unix-cmds/README.md) to selected Unix commands
- [link](https://en.wikibooks.org/wiki/Guide_to_Unix/Commands) to wiki guide to Unix commands
- simple example of [C compilation](files/7.md)
- [upgrading to Python 3.7](files/8.md) plus matplotlib
- [``$PATH``](files/5.md), a shaggy dog story
- [.bash_profile](files/5a.md)
- [link](http://linuxcommand.org/index.php) to a guide to learning the command line

[Here](http://www.ee.surrey.ac.uk/Teaching/Unix/) is a good introduction to Unix.

#### Python

[Here](python/README.md) are a few examples that I like and links to other things I've written about Python.

I developed a [program](python/bad-links.md) to check for broken links in this repo.

The official [Python tutorial](https://docs.python.org/3/tutorial/) is excellent.  And [here](https://github.com/telliott99/PyBioinformatics) is the source for a book that I wrote about using Python for Bioinformatics.  

The pages render fine as restructured text, but to get the real deal you need to use [Sphinx](http://www.sphinx-doc.org/en/master/).

<hr>

#### A bit more about SSH

- the [math](https://github.com/telliott99/CryptoQuickies/blob/master/public-key_math.md) of Public Key cryptography
- [generating](files/18.md) a Public/Private key pair
- a (slightly hokey) encryption [example](files/19.md)
- [ssh](files/17a.md) passphrase macOS quirk

#### General info about passwords

- my notes on [password complexity](named_files/pw_complexity.md)
- [generating](named_files/pw_util.md) passwords from the command line

<hr>

#### Current stuff

- Growing my [Linux Fu](linux/main.md)

#### Ideas for future projects

- [433 MHz receiver](https://www.princetronics.com/how-to-read-433-mhz-codes-w-raspberry-pi-433-mhz-receiver/) on Pi, other IOT stuff
- [LIRC](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/) --- control your TV
- GPIO [stuff](http://razzpisampler.oreilly.com/ch07.html)
- [weather station](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station)
- [touchscreen](https://www.pishop.us/product/official-raspberry-pi-7-touch-screen-display-with-10-finger-capacitive-touch/?src=raspberrypi)
- [hardcore](named_files/hardcore.md) software

I am keeping an eye on [Atomic Pi](https://www.kickstarter.com/projects/323002773/atomic-pi-a-high-power-alternative-to-rpi/updates) --- more [here](http://www.digital-loggers.com/api.html).  Order [here](https://dlidirect.com/products/atomic-pi).

Since these pages haven't been read much by others, there is a higher probability of errors or bugs than usual.  If you find one please let me know.