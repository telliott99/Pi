#### Binary grep

Seeking bytes in a binary file [page here](https://github.com/tmbinc/bgrep).

I just did

```
brew install bgrep
```

and tested 

```
> echo "abcdef" > x.txt
> hexdump -C x.txt
00000000  61 62 63 64 65 66 0a                              |abcdef.|
00000007
> bgrep "\x63" x.txt
invalid hex string!
> bgrep 63 x.txt
x.txt: 00000002
```

```
> echo "abc" > x.txt
> dd bs=1024 if=x.txt of=y.txt conv=sync
..
1024 bytes transferred ..
> bgrep "0000" y.txt | head -n 5
y.txt: 00000004
y.txt: 00000005
y.txt: 00000006
y.txt: 00000007
y.txt: 00000008
```

