#### Raspberry Pi memory

The Raspberry Pi does not have onboard disk drive for storage but instead the operating system, user files, etc. all reside on an SD card.  Since memory is expensive, this decreases the cost of the Pi.

And it is, in many respects, an advantage.  One can set up the Pi OS on a cheap 8 or 16 GB card, install a bunch of specialized software, and then remove the card and use it only when you need it.

#### the card

I had read that the Pi takes a standard 32 x 24 x 2.1 mm card, not a mini or micro, but this is not correct.

The Pi 3B+ has switched to **using a microSD card slot**.  

I got this [SD card](https://www.amazon.com/gp/product/B01H5ZNOYG/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1) because the blurb it says "works with all Raspberry Pi models" (which is only made possible by the fact that it is a micro card in an adapter). 

The card in the picture clearly says "Micro".

#### Formatting

The file system for the Pi is FAT32.

The Pi docs make a big deal of using the formatting software from the [SD Foundation](https://www.sdcard.org/downloads/formatter_4/index.html).

This is undoubtedly related to the fact that the Foundation says

> It is strongly recommended to use the SD Memory Card Formatter to format SD/SDHC/SDXC Cards rather than using formatting tools provided with individual operating systems

AFAIK, this is mostly due to historically poor performance of Windows formatters.  

Since I am starting with an officially sanctioned SD card pre-installed with NOOBS this isn't a problem.  

(NOOBS is of course a bit of a joke:  "newbies" are beginners).

On the Mac, Disk Utility or the command line works just fine for me.

> NOOBS – New Out Of the Box Software

I found official notes [here](https://www.raspberrypi.org/documentation/installation/noobs.md)

> Windows

> If you are a Windows user, we recommend formatting your SD card using the SD Association's Formatting Tool, which can be downloaded from sdcard.org. Instructions for using the tool are available on the same site.

> Mac OS

> The SD Association's Formatting Tool is also available for Mac users, although the default OS X Disk Utility is also capable of formatting the entire disk. To do this, select the SD card volume and choose Erase with MS-DOS format.

#### Mass storage devices

Booting from mass storage devices (like thumb drives, or even SSDs) is described as "in development."

This [USB drive](https://www.amazon.com/gp/product/B015CH1JIW/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1) works just fine for me.
