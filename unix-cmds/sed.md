#### sed

``sed`` can work on stdin or on a file:

```
> echo "abcabc" | sed 's/b/./'
a.cabc
```

Here it has only substituted for the first "b".  Compare with ``g`` (global):

```
> echo "abcabc" | sed 's/b/./g'
a.ca.c
```

For this example, ``printf`` and ``echo`` work the same.

``sed`` without ``g`` substitutes the first target *in each line*.

```
> cat z.txt
abc bca cab
bca cab abc
cab abc bca
> sed 's/b/./' z.txt
a.c bca cab
.ca cab abc
ca. abc bca
> sed 's/b/./g' z.txt
a.c .ca ca.
.ca ca. a.c
ca. a.c .ca
```

#### regular expressions

``sed '/^#/ d'`` means "find all lines that start with # and delete them", so for example:

```
> cat x.txt
# comment
abc
# another comment
def
ghi # a third one
> sed '/^#/ d' x.txt
abc
def
ghi # a third one
```

The ``^`` means to match only if the first character is ``#``.

Here is an example from the other day.  Our script ``setup`` has a lot of comments and a lot of empty lines:

```
> cat setup | head -n 4
#! /bin/bash
echo "in setup"

cd tmp
> sed '/^#/ d' setup | head -n 4
echo "in setup"

cd tmp

```

``sed '/^#/ d'`` deletes lines starting with ``#``.

``sed '/^$/ d`` deletes empty lines.

```
> sed '/^#/ d' setup | sed '/^$/ d' | head -n 4
echo "in setup"
cd tmp
mkdir ~/.ssh
cp key ~/.ssh/authorized_keys
```

We take the first four lines of the original:  1 comment and 1 empty line.  Remove the comment ``^#``, then the empty lines.  Print the first four lines of the result.

 (``^$`` means the beginning ``^`` and the end ``$`` of the line are immediately next to one another).