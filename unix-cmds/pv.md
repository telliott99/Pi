#### Progress viewer

[link](https://askubuntu.com/questions/215505/how-do-you-monitor-the-progress-of-dd)

For a long-running command like ``dd`` you'd like to check its progress to be sure it's still running and didn't hang up.

A newer method no need for su or pv:

```
dd bs=1024 count=1000 if=/dev/urandom of=/dev/null status=progress
```

But macOS doesn't have it.

Alternatively, this works

```
brew install pv
> dd  bs=1m count=100 if=/dev/urandom | pv | dd of=/dev/null
```

Might play with ``-s`` flag to ``pv``.

Also

method 0

```
> sudo kill -INFO $(pgrep ^dd)
Password:
```
