#### Symbolic links with ln

Silly example

```
> cd Desktop
> mkdir tmp
> touch tmp/x
> ln -s y tmp/x
ln: tmp/x: File exists  # wrong direction!
> ln -s tmp/x y
```

On the man page, the first file (``y``) is called the "source_file" but I would think of it as the destination.  The second file is called the "target", also opposite to my thinking.

**ln -s <to-file> <from-file>**

```
> echo "abc" >>y
> cat y
abc
> cat tmp/x
abc
> 
```

A classic use is in web or ssh server configuration.

```
pi@raspberrypi:/etc/apache2 $ ls -al /etc/apache2/mods-enabled/
total 8
drwxr-xr-x 2 root root 4096 Feb 24 15:34 .
drwxr-xr-x 8 root root 4096 Feb 24 15:34 ..
lrwxrwxrwx 1 root root   36 Feb 24 15:34 access_compat.load -> ../mods-available/access_compat.load
lrwxrwxrwx 1 root root   28 Feb 24 15:34 alias.conf -> ../mods-available/alias.conf
..
```

The contents of ``..enabled`` or symbolic links to the actual content, which is in ``..available``.  This makes activation and inactivation a simple matter of manipulating the symbolic link.