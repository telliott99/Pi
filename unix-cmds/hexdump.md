#### hexdump

extra material

#### ``-s`` (skip) flag

Make a file with 2K of random sequence
dd bs=1024 count=2 if=/dev/random of=tmp conv=sync

```
hexdump -C -n 16 -s 1k tmp
00000400  04 e9 05 cd 57 ca 2b c9  ea 63 b6 21 ae 76 af d7  |....W.+..c.!.v..|
00000410

> hexdump -C -n 16 -s 16 tmp
00000010  57 15 5c e4 8d 3c 8a ad  8a 8f 65 02 d6 6c 73 56  |W.\..<....e..lsV|
00000020
```

The ``-s`` flag is an offset

> By default, offset is
interpreted as a decimal number.
With a leading 0x or 0X, offset is
interpreted as a hexadecimal number,
otherwise, with a leading 0, offset
is interpreted as an octal number.
Appending the character b, k, m, or g
to offset causes it to be interpreted
as a multiple of 512, 1024, 1048576,
or 1073741824, respectively.