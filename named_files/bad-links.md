There's a lot of rearranging that goes into a project like this one.  When you do that, it is very hard to remember which files link to the one you are moving to a new location.

I wrote two Python scripts 

- [find.py](../python-scripts/find.py)
- and a helper [utils.py](../python-scripts/utils.py)

to check for broken links in a repo.

Here are some of the highlights.

#### directory listing

```
import subprocess
..
out = subprocess.check_output(['find', d])
```

We could use Python to go through directories and sub-directories, but this is easier.  Just launch a Unix process and run ``find`` on the directory that we're passed on the command line.

#### Patterns

We are searching for links to files and images, which have distinctive patterns like:

- ``'![](path)'``
- ``'<img src="../super/fn.png" ... />``
- ``'[app.py](app.py)'``
- ``'[name](../path/to/file.md)'``

Regular expressions are used to find these.  

I find this subject challenging, so I'll keep it basic.

#### Python regular expressions

Suppose we want a line beginning with ``'a'``.  That is signified by ``'^a'``:

```
>>> import re
>>> p = re.compile(r'^a')
>>> t = 'abc'
>>> p.search(t)
<_sre.SRE_Match object at 0x106da3168>
>>> m = p.search(t)
>>> m.group(0)
'a'
>>> p.search('bac')
>>> 
```

Notice the lack of a match for the second target.

In the case of ``'[app.py](app.py)'``, we're looking for the pattern ``'[name](link)'``.

In searching for ``[``, we must escape the character, because it has a special meaning for regexes, namely, ``[abc]`` searches for *any* of ``abc`` or, for that matter, any of ``[a-z]``.

Something like this:

```
>>> p = re.compile(r'\[.+\]')
>>> m = p.search('[name](link)')
>>> m.group(0)
'[name]'
>>>
```

The ``.+`` is a dot ``.``, which matches any character except a newline, and ``+`` means one or more of the preceeding character.

Now, the ``'('`` character is not *special*, so it must not be escaped:

```
>>> p = re.compile(r'\[.+\](.+)')
>>> m = p.search('[name](link)')
>>> m.group(0)
'[name](link)'
>>>
```

This does not match 

```
>>> p = re.compile(r'\[.+\](.+)')
>>> m = p.search('![](link)')
>>> m
>>> 
```

However, this does:

```
>>> p = re.compile(r'\[.?\](.+)')
>>> m = p.search('![](link)')
>>> m
<_sre.SRE_Match object at 0x1065c0918>
>>> m.group(0)
'[](link)'
>>>
```

As I say, I'm not that swift with this.  In some cases things didn't work, and I couldn't figure it out quickly enough, so I fall back on old methods like:

```
>>> s = '<img src="../super/fn.png" ... />'
>>> i = s.find('"')
>>> j = s.find('"',i+1)
>>> ret = s[i+1:j]
>>> ret
'../super/fn.png'
>>>
```

#### Reporting results

At the end of the script I want to say something like:  "we searched ``n`` files and ``g`` of them were OK".

```
OK_files = dict()
run(OK_files)
D = OK_files
good = sum( [1 for k in D.keys() if D[k]] )
t = (len(D.keys()), good)
print('%d files searched: %d OK' % t) 
```

I used a global variable, a dictionary, which gets passed into ``run`` and then into ``check``.  For each new filename, we set a key in the dictionary to ``True``.

If, for any of possibly multiple links in a file, we have a problem:

```
if not os.path.exists(path):
    ..
    D[fn] = False
```

#### Running the script

In its current configuration in the file system, you can drag the filenames to Terminal.

So doing something like this is just a matter of two drag operations:

```
> python ~/Dropbox/Github/Pi/python-scripts/find.py \
~/Dropbox/Github/Pi 
137 files searched: 137 OK
>
```

However, normally I use an alias for the second path and run the script from the Desktop (with ``utils.py`` also present there):

```
python find.py $ghd/Pi
```