##### dd

#### typical usage

```
sudo dd bs=1m if=/os.img of=/dev/rdisk2 conv=sync
```

#### details

The ``dd`` command does something extremely simple, it

> The dd utility copies the standard input to
the standard output.  Input data is read and
written in 512-byte blocks.  If input reads
are short, input from multiple reads are
aggregated to form the output block.

If you provide an ``if`` or ``of`` argument, then these are substituted for stdin or stdout.  

``dd`` requires ``sudo`` (always?) for the basic reason that if the ``of`` argument is something like ``/dev/rdisk1`` you are screwed.

(Note:  you must ``diskutil unmountDisk`` a disk to ``dd`` to it).

The argument ``bs`` (block size) is often given.  The default is 512-byte blocks.

What's the best size to specify?

The other common argument is ``conv``, where we usually do ``conv=sync``.  From the man page, about ``conv=sync``:

> Pad every input block to
the input buffer size.
Spaces are used for pad
bytes if a block oriented
conversion value is speci-
fied, otherwise NUL bytes
are used.

#### count

> count=n  Copy only n input blocks.

I found this *very* useful.  Suppose ``if`` is some disk.  Then ``dd`` will copy the whole disk, unless you specify when to stop.

So if you want to copy 2 GB and your block size is ``1m``, then set ``count=2000`` and you are good.

Note:  on the Pi, ``1m`` isn't valid input.  It wants ``1M``.  Go figure.


#### watch progress

[this]() says:

```
watch -n5 'sudo kill -INFO $(pgrep ^dd)'
```

will do it