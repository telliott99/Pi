#### xargs

#### example 1

Suppose we want to find every place in the project where a particular filename is mentioned (maybe we need to change all such mentions to something else):  ``named_files``.

- First attempt

```
find $ghd/Pi | grep "named_files"
```

(``$ghd`` is an alias for my github directory).

output:

```
> find $ghd/Pi | grep "named_files" | head -n 4
..named_files
..named_files/locale.md
..named_files/.DS_Store
..named_files/pw_complexity.md
```

This is fine so far as it goes.  We ``grep`` the result from ``find`` as a single file.

I chopped off the long output corresponding to ``$ghd/Pi`` above.  That part is

```
> echo $ghd/Pi | wc
       1       1      40
```

40 characters, so I can do the same thing more efficiently with ``cut``

```
> find $ghd/Pi | grep "named_files" | cut -c 41-
named_files
named_files/locale.md
named_files/.DS_Store
named_files/pw_complexity.md
..
```

However, what we really want is to look at the contents of the individual files.  

That's where ``xargs`` comes in. It feeds the filenames one at a time to the command that follows.


- Second attempt

```
find $ghd/Pi | grep -vE ".git|.DS" \
| xargs grep "named_files"
```

I've improved the efficiency of the search by first removing all the git files and ``.DS`` Finder nonsense.

The backslash ``\`` allows the command to continue onto the next line and makes it easier to see all the pieces.

At this point, I get a lot of complaints from ``grep`` (the second one) that ``.. is a directory``.

We change the find invocation to return only files and not directories (``-type f`` flag), but there are also a few other complaints, which I just silence with ``2>/dev/null``:

- Third attempt

```
find $ghd/Pi -type f \
| grep -vE ".git|.DS" \
| xargs grep "named_files" 2>/dev/null \
| cut -c 41-100 \
| head -n 4
```

output:

```
> find $ghd/Pi -type f | grep -vE ".git|.DS" | xargs grep "named_files" 2>/dev/null | cut -c 41-100 | head -n 4
disk-stuff/README.md:- [quick reference](named_files/headles
disk-stuff/backup3.md:We copy over [``wpa_supplicant.conf``]
README.md:So I [ordered](named_files/orders.md) a few things
README.md:- [file systems](named_files/file-systems.md) or w
> 
```

One last tweak is to realize that line numbers would be helpful.  We get that with the ``-n`` flag to ``grep``:

```
> find $ghd/Pi -type f | grep -vE ".git|.DS" | xargs grep -n "named_files" 2>/dev/null | cut -c 41-100 | head -n 4
disk-stuff/README.md:36:- [quick reference](named_files/head
disk-stuff/backup3.md:35:We copy over [``wpa_supplicant.conf
README.md:5:So I [ordered](named_files/orders.md) a few thin
README.md:33:- [file systems](named_files/file-systems.md) o
>
```

How many such files are there?

```
> find $ghd/Pi -type f | grep -vE ".git|.DS" | xargs grep -n "named_files" 2>/dev/null | cut -c 41-100 | wc -l
      12
>
```

Not so many.

#### example 2:  SLOC

Suppose we want to know how many lines of Python code there are in the project.

```
find $ghd/Pi -type f | grep ".py$" > x.txt
```

We ``grep`` for file names ending in ``.py``.  This misses a few.  But those all contain within them as the first line ``!# /usr/bin/python*``.

That's a job for ``xargs``.

```
find $ghd/Pi -type f \
| xargs grep -l "#\!.*python" 2>/dev/null > y.txt
```

We take each file from ``find``, feed it line by line to ``grep`` (``-l`` suppresses the match output, just gives the filename back if it matches).  The pattern is

```
"#\!.*python"
```

The ``!`` is special, so it's escaped.  And ``.*`` allows any number of characters before ``python``.

To be safe, save this in a second file.  Then:

```
cat x.txt y.txt | uniq | xargs sed '/^$/d' > z.txt
```

There are a few dups between ``x`` and ``y`` so ``uniq`` takes care of that.  Then

```
sed '/^$/d'
```

deletes (``d``) the lines that begin ``^`` and end ``$`` with nothing in between (empty lines).

Finally, 

```
cat z.txt | grep -v "#" | wc -l
```

Inverse ``-v`` ``grep`` grabs all the lines that don't contain ``#`` and then we count them.

```
> cat z.txt | grep -v "#" | wc -l
    1151
```

Not bad.