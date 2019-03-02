#### ``disk`` and ``rdisk`` on macOS 

[here](https://superuser.com/questions/631592/why-is-dev-rdisk-about-20-times-faster-than-dev-disk-in-mac-os-x)

From ``man hdiutil``

> /dev/rdisk nodes are character-special devices, but are "raw" in the BSD sense and force block-aligned I/O. They are closer to the physical disk than the buffer cache. /dev/disk nodes, on the other hand, are buffered block-special devices and are used primarily by the kernel's filesystem code.

Why would you want buffering?

> Because caching is still a desirable thing. In cases where you have removable media, you want to get the data on the physical device as fast as possible, because you want the data in another physical location. Internal hard drives are a different story. You usually don't carry them around, so you don't care when the data is actually written to the device. When you cache data written to/read from devices that's a more expensive way of writing to the disk, but your programs are still faster, since they don't need to wait until all the data they want to write is written to the disk.