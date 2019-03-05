#### grep

#### basic

``grep < pattern > < file >``

but also

``< cmd > | grep < pattern >``

e.g.

``history | grep "erase"``

Simple regular expression chars:  ``^`` and ``$``

```
> cat x.txt
abc
bca
cab
> grep "^a" x.txt
abc
> grep "a" x.txt
abc
bca
cab
> grep "b$" x.txt
cab
```

#### two patterns

```
> printf "foo\nbar\nbaz\n" > x.txt
> grep 'foo\|bar' x.txt
foo
bar
> grep -E 'foo|bar' x.txt
foo
bar
```

So ``-E`` or ``\|``.

#### inverted

- ``-v`` invert match, non-matching lines only

```
> grep -v "^a" x.txt
bca
cab
```

#### more flags

- ``-n`` --- line number of the match
- ``-r`` (recursive) descend into a directory

Example:

```
> grep -nr "abc" .
...
../x.txt:1:abc
...
./grep.md:11:abc
./grep.md:15:abc
./grep.md:17:abc
./grep.md:32:> grep -nr "abc" .
./grep.md:34:./grep.md:abc
```

- ``-i`` --- ignore case
- ``-c`` --- print a count of number of matching lines

So

```
> grep -ci "A" x.txt
3
```

#### context

- ``-A`` print A lines of context after each match
- ``-B`` print B lines before each match
- ``-C`` print C lines before and after each match

#### regex

The patterns that grep searches for are called regular expressions, or regex for short.  regex is a language defining descriptions of search patterns that are not necessarily exact matches.

Some simple regex symbols and patterns are:

- ``*`` wildcard
- ``\d`` matches a digit [0-9]
- ``\D`` matches a non-digit
- ``\s`` matches whitespace
- ``^`` match only at the beginning of the string
- ``$`` match only at the end of the string
- ``[abc]`` match any of a,b,c
- ``[a-d]`` match any of a,b,c,d

#### more

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

