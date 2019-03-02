#### sudo

``sudo`` is traditionally explained as "super-user do once", but is likely related to ``su`` which stands for "substitute user."

#### Adding sudo

It's common to discover that a command entered without ``sudo`` didn't execute because ``sudo`` is needed.  You can use the up-arrow to list the previous command and then ``CTRL+A`` will move the cursor to the beginning of the line and you can type ``sudo`` or ...

- ``sudo!!`` repeats the last command with sudo added

#### ``su`` and ``sudo``

According to ``man su``

```
su -- substitute user identity

The su utility requests appropriate user cre-
dentials via PAM and switches to that user ID
(the default user is the superuser).  A shell
is then executed.
```

Try

```
> echo $UID
501
> su
Password:
sh-3.2# echo $UID
0
sh-3.2# exit
exit
>

```

By default, the environment is unmodified
 with the exception of USER, HOME, and SHELL.
 
#### ``sudoers``

Behavior is determined in a complicated was on macOS.  The Pi is simpler

One determinant is the ``/etc/sudoers`` file.

``/etc/sudoers`` *must* be edited by entering ``visudo``.  (As usual, ``i`` to insert, ``ESC`` to leave edit mode, :wq to write and quit).

I modified ``etc/sudoers`` on the Mac according to [this](http://osxdaily.com/2016/05/05/change-sudo-password-timeout/) by adding

```Defaults    timestamp_timeout=60```

which does appear to increase the time from the usual 5 minutes.

On the Pi, no password is needed.  At the end of ``/etc/sudoers`` is this line

```
#includedir /etc/sudoers.d
```

and ``/etc/sudoers.d/010_pi-nopasswd`` has one line:

```
pi ALL=(ALL) NOPASSWD: ALL
```
meaning

```
pi hosts=(users) NOPASSWORD: cmds
```

User ``pi`` can switch on all hosts can switch to all users.

User ``pi`` doesn't need password for all commands (including ``sudo``).

[notes](https://raspberrypi.stackexchange.com/questions/7133/how-to-change-user-pi-sudo-permissions-how-to-add-other-accounts-with-different)

 