#### find

Most often I use ``find`` to list all the files in a directory and send the result to ``grep``, with or without ``xargs``.  Those uses are described under [grep](grep.md) or [xargs](xargs.md).

#### flags for ``find``

- ``-exec``
- ``-type f`` 
- ``-maxdepth 1``
- ``-exclude-dir dirname``
- ``-name``
- ``-newer`` (see [``touch``](touch.md))
- ``-mtime``

#### by name

- ``-name``

To find a single file by name in a big directory:

```
> find $ghd -name eratosthenes.py
../Pi/python-scripts/eratosthenes.py
```

#### exclude hidden files

- ``-not -path '*/\.*'``

```
> find $ghd/Pi/flask -type f -not -path '*/\.*' | head -n4
/Users/telliott_admin/Dropbox/Github/Pi/flask/forms/config.py
/Users/telliott_admin/Dropbox/Github/Pi/flask/forms/app/__init__.py
/Users/telliott_admin/Dropbox/Github/Pi/flask/forms/app/templates/hello.html
/Users/telliott_admin/Dropbox/Github/Pi/flask/forms/app/templates/time.html
```

#### modification time

- ``-mtime``

Find all files modified in the last day:

```
> find $ghd -mtime -1 | wc -l
      89
```

Without the dash on ``-1`` it's exact.

Many of those are git-related.  Use grep to fix that.

What about the last 10 minutes?

```
> cd $ghd
> find . -mmin -10
./Pi/unix-cmds
./Pi/unix-cmds/find.md
./Pi/unix-cmds/README.md
>
```

#### find and do something

```
find ./ -type f -exec sed -i 's/target/replace/g' {} \;
```

