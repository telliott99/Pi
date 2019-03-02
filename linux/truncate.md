####  Truncate

#### Preliminary

```
> echo "abc" > x.txt
> hexdump -C x.txt
00000000  61 62 63 0a                                       |abc.|
00000004
> sudo dd bs=1024 if=x.txt of=y.txt conv=sync
Password:
0+1 records in
1+0 records out
1024 bytes transferred in 0.000101 secs (10129640 bytes/sec)
> stat -f %z y.txt
1024
> 
```

#### Use

The man page for truncate is there but not the command itself, on macOS.  Use Homebrew

```
brew install truncate
truncate y.txt -s 16
> stat -f %z y.txt
16
```

Works great.  Note ``cat`` is not a reliable tool to use to determine file size.

Suppose I want to construct a decent sized file with a lot of null bytes on the end.

We could obtain null bytes from ``/dev/zero``.  We tested ``pv`` this way

```
> dd bs=1024 count=100000 if=/dev/zero | pv | dd of=/dev/null
100000+0 records in
100000+0 records out
102400000 bytes transferred in 0.804205 secs (127330727 bytes/sec)
97.7MiB 0:00:00 [ 121MiB/s] [<=>                       ]
200000+0 records in
200000+0 records out
102400000 bytes transferred in 0.805422 secs (127138309 bytes/sec)
>
```

so

```
> sudo dd bs=1024 if=x.txt of=y.txt conv=sync
> stat -f %z y.txt
1024
> dd if=/dev/zero bs=1000 count=2000 >> y.txt
2000+0 records in
2000+0 records out
2000000 bytes transferred in 0.015582 secs (128352531 bytes/sec)
> stat -f %z y.txt
2001024
```

now test gzip to remove them

```
> stat -f %z y.txt
2001024
> gzip -c y.txt > y.txt.gz
> gunzip -c y.txt.gz > yy.txt
> stat -f %z yy.txt
```

``2001024``.  Nope.

``sed``

```
sed '$ s/\x00*$//' y.txt
stat -f %z y.txt
```

``2001024``.  Nope.

According to what I've seen, ``dd`` is the right tool.  But you have to know how many bytes to trim.

Another [problem](https://unix.stackexchange.com/questions/6852/best-way-to-remove-bytes-from-the-start-of-a-file)

```
> dd bs=1 skip=1 if=x.txt of=y.txt
3+0 records in
3+0 records out
3 bytes transferred in 0.000086 secs (34856 bytes/sec)
> cat y.txt
bc
>
```

That works!