#### hdiutil

According to [this](http://commandlinemac.blogspot.com/2008/12/using-hdiutil.html), ``hdiutil`` is a native Apple command line utility.  ``hdi``: hard drive *image*.

From ``man hdiutil``

>  hdiutil uses the DiskImages framework to
 manipulate disk images.  Common verbs include
 attach, detach, verify, create, convert, and
 compact.


- ``hdiutil mount <img-name>``
- ``hdiutil unmount /dev/<dev-name>``

All removable media are mounted in ``/Volumes``.

``<dev-name>`` would typically be like ``/dev/disk2s1``;  it will also have a name ``Volumes/<mountpoint>``.

- ``hdiutil create <x.dmg> -srcfolder /path/to/folder/``
- ``hdiutil create -encryption -size 10m -volname encdata test.dmg -fs HFS+J``

