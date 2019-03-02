#### borking my USB drive

After stopping the copy with ``CTRL-C``, my drive wouldn't show up when I unplugged and replugged it.

In desperation, I tried:

```
sudo mount /dev/disk2
```

which, amazingly, resuscitated it!