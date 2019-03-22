#### touch

> change the file access and modification times

I mostly use this to create a file with no filetype extension or one which TextEdit would pester me about:

```
touch x.md
```

and then double-click the icon to edit with macdown. Or use my ``te`` alias

```
te x.md
```

#### Change modification or access times

```
> touch -mt 201903120000 x
> ls -al x
-rw-r--r--  1 telliott_admin  staff  0 Jan 12  2008 x
> find . -newer x
..
./doughnut_and_coffee_cup.gif
..
```

#### Notes

The default is to follow a symbolic link.

```
> touch x
> ln -s x y
> ls x
x
> ls -al x
-rw-r--r--  1 telliott_admin  staff  0 Feb 24 12:13 x
> touch y
> ls -al x
-rw-r--r--  1 telliott_admin  staff  0 Feb 24 12:14 x
>
```

The ``-h`` flag prevents modification of the link, but changes the file that is linked to

```
> touch y -h
> ls -al y
lrwxr-xr-x  1 telliott_admin  staff  1 Feb 24 12:13 y -> x
> ls -al x
-rw-r--r--  1 telliott_admin  staff  0 Feb 24 12:15 x
```