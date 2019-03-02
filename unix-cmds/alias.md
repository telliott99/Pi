### Aliases

Here's a silly example:

```
> copy
-bash: copy: command not found
> alias copy=cp
> copy x.txt y.txt
```

However, the usual idea is to make commonly used commands shorter, not longer.  Also, the alias above lives only as long as that Terminal session.  

We would like some way to make it available always.

#### Changing host keys for ssh

When we connect to an ipaddress with ssh like
> ssh pi@10.0.1.7

the client OS (that's us) checks whether the server's public key matches what's in ``~/.ssh/known_hosts``, and if there is no entry, then it gives a warning about accepting a new key.

OTOH, if there is an entry, but the key is not a match, then the connection is denied.

<hr>

Every time we boot a copy of Raspbian for the first time, it generates a new server key pair, which can lead to a mismatched keys problem.

#### Solution 1

Use ``ssh-keygen``

```
> ssh-keygen -R 10.0.1.7
```

#### Solution 2

I defined an alias in my ``~/.bash_profile``:

```
alias kh="cp ~/.ssh/known_hosts.cache ~/.ssh/known_hosts && echo '10.0.1.7 removed'"
```

``kh`` stands for "kill host".

Be sure to check to make sure ``kh`` isn't defined already.

Then I made a cache of the file, edited to remove the key for 10.0.1.7.  To refresh, I can just do:

```
> kh
10.0.1.7 removed
```

I also have some git-related ones:

```
alias gita="git add .; git commit -m 'no message'"
alias gitp="git push -u origin master"
```

#### Compare to variable

The [difference](https://stackoverflow.com/questions/7342735/bash-command-whats-the-difference-between-a-variable-and-an-alias) between an alias and a variable:

> Variables are much more versatile than aliases. Variables can be used anywhere in a command line (e.g. as parts of program arguments), whereas aliases can only be used as the names of programs to run, i.e. as the first word in a command line. For example:

> Variables can also be exported into the environment of child processes. If you use the export builtin to export variables, then programs can use getenv(3) function to get the variables' values.

```
export FOO=BAR
```

FOO is a variable, to reference it use $FOO, as in

```
> export FOO=BAR
> echo $FOO
BAR
```

From Python

```
> export FOO=BAR
> python
..
>>> import os
>>> print(os.environ['FOO'])
BAR
>>> 
```

```
>>> for k in os.environ:
...     print k, os.environ[k]
... 
TERM_PROGRAM_VERSION 421.1
LOGNAME telliott_admin
USER telliott_admin
PATH /Users/telliott_admin/bin:/Users/telliott_admin/Library/Python/2.7/bin:/Users/telliott_admin/Library/Python/3.6/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin
HOME /Users/telliott_admin
TERM_PROGRAM Apple_Terminal
LANG en_US.UTF-8
__CF_USER_TEXT_ENCODING 0x1F5:0x0:0x0
TERM xterm-256color
Apple_PubSub_Socket_Render /private/tmp/com.apple.launchd.V4nO9kELlj/Render
PW verysecret
SHLVL 1
XPC_FLAGS 0x0
TMPDIR /var/folders/1l/d7lmw_ln5hb933r7jbkt6mq00000gn/T/
TERM_SESSION_ID EAE3AB2E-E19E-41FB-B805-FCB14A46FBDF
XPC_SERVICE_NAME 0
SSH_AUTH_SOCK /private/tmp/com.apple.launchd.ZP8omkWpFI/Listeners
SHELL /bin/bash
FOO BAR
_ /usr/local/bin/python
OLDPWD /Users/telliott_admin
ghd /Users/telliott_admin/Dropbox/Github
PWD /Users/telliott_admin/Desktop
>>> 
```