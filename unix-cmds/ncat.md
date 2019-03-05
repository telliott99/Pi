#### ``ncat`` (netcat)

So ``nc`` and ``ncat`` are different, at least on macOS.

[link](https://www.linuxtechi.com/nc-ncat-command-examples-linux-systems/)

#### listen

```
ncat -l 8080
```

In another window:

```
> ncat localhost 8080
HEAD / HTTP/1.1
```

The first window shows the command is received.