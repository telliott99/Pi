#### kill

In the context of using the ``kill`` command on a process, you can use number equivalents:

``kill -< signal name/number > < pid >``

```
Some of the more commonly used signals:

     1       HUP (hang up)
     2       INT (interrupt)
     3       QUIT (quit)
     6       ABRT (abort)
     9       KILL (non-catchable, non-ignorable
             kill)
     14      ALRM (alarm clock)
     15      TERM (software termination signal)
```

``^C is -2, ^Z is -9``.

#### Interesting use:

I used ``kill`` to get info on a long-running process.  The process will print info in response to the ``INFO`` signal.

```
> sudo kill -INFO $(pgrep ^dd)
Password:
```

It needs ``sudo`` because ``dd`` needs ``sudo``.
