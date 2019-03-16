#### Control characters (Linux)

- ``CTL-C``
- ``CTL-D``
- ``CTL-Z``

[link](https://unix.stackexchange.com/questions/110240/why-does-ctrl-d-eof-exit-the-shell)

#### ``^D``

``CTRL-D``, or ``^D``, also known as ``\04`` or 0x4, is called END_OF_TRANSMISSION in Unicode.

It is the default EOF control character for the shell.  Thus:

```
> spi
Last login: Mon Mar  4 09:39:59 2019 from fe80::c81:f1f1:2736:50c9%wlan0
pi@raspberrypi:~ $
```

I enter ^D here but the shell shows:

```
pi@raspberrypi:~ $ logout
Connection to raspberrypi.local closed.
> 
```

#### ``^Z``

[link](https://superuser.com/questions/262942/whats-different-between-ctrlz-and-ctrlc-in-unix-command-line)

- ``CTRL+C`` or ``^C`` sends a process SIGINT
- ``CTRL+Z`` or ``^Z`` sends a process SIGSTP

**SIGSTOP** allows the program to cleanup after itself. 

**SIGINT** cannot be intercepted by the program.

```
> cat
^Z
[1]+  Stopped                 cat
> cat
^C
>
```

``^Z`` is more severe than ``^C``

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
