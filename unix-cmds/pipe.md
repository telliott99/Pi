#### Pipes, etc.

``>`` means to write the output of a command to a specified file.

```
> echo "abc" > x.txt
> cat x.txt
abc
> printf "abc" > y.txt
> cat y.txt
abc>
```

(``printf`` doesn't add a newline in the default mode).

<hr>

``|`` means to "pipe" the output of one command to another, like this:

```
> history | grep "dd"
 396  sudo dd bs=1M if=os.img of=/dev/rdisk2 conv=sync

```

To actually run command 396 from your history, type ``!396``.

<hr>

``>>`` means to append the output to a specified file.

```
> echo "abc" > x.txt
> echo "def" >> x.txt
> cat x.txt
abc
def
```

Both stdout *and* stderr are redirected.

<hr>

``<`` means to use the specified file as input

```
> printf "abc\ndef\n" > x.txt
> grep "d" < x.txt
def
>
```

<hr>

``stdout`` and ``stderr`` can also be redirected.

To discard or ignore error messages, do

```
myscript.sh 2>/dev/null
```

example:

```
> ls z
ls: z: No such file or directory
> ls z 2>/dev/null
>
```

```
myscript.sh 2>&1 >> x.txt
```

This directs stderr ``2`` to stdout ``&1`` (address of ``1``), and the ``>>`` directs stdout (only) to the specified file.  



