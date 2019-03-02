#### File Systems

AFAIK the original Windows PC file system was [FAT](https://en.wikipedia.org/wiki/File_Allocation_Table#Historical_evolution), which stands for File Allocation Table.  

Later versions include FAT12, FAT16 and [FAT32](https://en.wikipedia.org/wiki/File_Allocation_Table#FAT32).

The numbering is a bit complicated, although naturally, larger is better.

> Cluster values are represented by 32-bit numbers, of which 28 bits are used to hold the cluster number. The boot sector uses a 32-bit field for the sector count, limiting the FAT32 volume size to 2 TiB for a sector size of 512 bytes and 16 TiB for a sector size of 4,096 bytes.

FAT32 was introduced in 1996.

**important size limitation**

> The maximum possible size for a file on a FAT32 volume is 4 GiB minus 1 byte or 4,294,967,295 (232 − 1) bytes.
>

[exFAT]() (ex for extended) is yet another Windows file system, introduced in 2006.  exFAT is optimized for flash storage.  It has a huge maximum volume size (128 PB), but it is also proprietary.

[NTFS]() stands for New Technology File System, and it was first introduced in 1993 with Windows.  NTFS is a more modern file system and has significant advantages for users who only use Windows.  

The disadvantage for us is that Mac OS X and now macOS, support read-write for FAT32, but NTFS is read only.  Apple has "experimental" support for writing NTFS but it is buggy. [link](https://www.howtogeek.com/177529/htg-explains-why-are-removable-drives-still-using-fat32-instead-of-ntfs/)  An area for future exploration.

There are third-party paid solutions (e.g. [Paragon](https://www.paragon-software.com/us/home/ntfs-mac/)).  These are also reported to be buggy.

If you run Macs but sometimes need to transfer data to Windows machines on a "stick" or "thumb drive", you will know the solution is to format the thumb drive to FAT32.  It's no good showing up at the UPS store with HFS+ (Journaled or not).

#### Mac OS

The standard Mac file system for many years (at least since 1998) was called HFS+ which also comes in a (Journaled) format.

A recent change is the Apple File System (APFS), which became standard for macOS with OS 10.13 and iOS 10.3.  Read about it [here](https://www.imore.com/apfs).

#### Linux

The standard Linux file system is extX or EXTX, where X is 2, 3, or 4.  macOS has no support for reading or writing ext.  This has practical implications when reading a card or drive taken from the Pi and examined on the Mac.  The Linux partition isn't readable so it isn't even visible.