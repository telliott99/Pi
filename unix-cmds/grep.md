#### Using grep

You ran a complicated command and you can't remember it:

```
> history | grep "dd"
..
437  sudo dd bs=1m if=os.img of=/dev/rdisk2 conv=sync
..
```

So then you do ``!437`` and run it again.

or you can't remember where the file ``pancakes.txt`` is so

```
> cd ~/Dropbox/Food
> find . | grep "pancakes"
./@write-ups/pancakes.txt
>
```

or you want to find files containing the line ``stuff"

```
> grep -r -n "stuff" ~/Github/MyUnix/ 
..MyUnix/basics/sphinx.rst:81:It can happen that partially built stuff..
>
```

[more](https://github.com/telliott99/UnixQuickies/blob/master/grep.md)

