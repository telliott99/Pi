#### diskutil

[link1](http://www.theinstructional.com/guides/disk-management-from-the-command-line-part-1), [link2](http://www.theinstructional.com/guides/disk-management-from-the-command-line-part-2), [link3](http://www.theinstructional.com/guides/disk-management-from-the-command-line-part-3)

> diskutil manipulates the structure of local
disks.  It provides information about, and
allows the administration of, the partition-
ing schemes, layouts, and formats of disks.

- diskutil list
- diskutil list <disk-id>   # like disk2
- diskutil info disk2s1
- diskutil activity
- diskutil unmount | umount [force]
- diskutil eject

- diskutil mount         # mount a single volume
- diskutil mountDisk     # all mountable volumes

So unmount, by itself, is a volume;  unmountDisk is all volumes on a disk and the disk itself.

example:

- diskutil partitionDisk /dev/disk2 2 MBR MS-DOS TE 2G "Free Space" FOO 0

2 means 2 partitions:
- MBR-DOS TE 2G
- "Free Space" Foo 0


```
> diskutil listFilesystems
Formattable file systems

These file system personalities can be used for erasing and partitioning.
When specifying a personality as a parameter to a verb, case is not considered.
Certain common aliases (also case-insensitive) are listed below as well.

-------------------------------------------------------------------------------
PERSONALITY                     USER VISIBLE NAME                               
-------------------------------------------------------------------------------
APFS                            APFS                                            
  (or) APFSI
Case-sensitive APFS             APFS (Case-sensitive)                           
ExFAT                           ExFAT                                           
Free Space                      Free Space                                      
  (or) FREE
MS-DOS                          MS-DOS (FAT)                                    
MS-DOS FAT12                    MS-DOS (FAT12)                                  
MS-DOS FAT16                    MS-DOS (FAT16)                                  
MS-DOS FAT32                    MS-DOS (FAT32)                                  
  (or) FAT32
HFS+                            Mac OS Extended                                 
Case-sensitive HFS+             Mac OS Extended (Case-sensitive)                
  (or) HFSX
Case-sensitive Journaled HFS+   Mac OS Extended (Case-sensitive, Journaled)     
  (or) JHFSX
Journaled HFS+                  Mac OS Extended (Journaled)                     
  (or) JHFS+
```