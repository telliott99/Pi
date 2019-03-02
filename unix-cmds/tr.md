```
> echo 'abc' > x.txt
> dd bs=1024 if=x.txt of=y.txt conv=sync
0+1 records in
1+0 records out
1024 bytes transferred in 0.000110 secs (9296466 bytes/sec)
> stat -f %z y.txt
1024
```


```
> tr < y.txt -d '\00' > z.txt
> stat -f %z z.txt
4
```