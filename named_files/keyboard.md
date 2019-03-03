The bash shell has something called Tilde expansion.  If a word begins with ``~`` (unquoted), then if there's nothing else there the tilde is replaced with the value of the HOME shell variable.

So ``~ `` with a space is the same as $HOME.

It would have been handy the other day when struggling with a keyboard layout that didn't have ``~`` in the upper left.  (Although it turns out to be where ``|`` is).  And ``|`` maps to a key (left of ``z``) that isn't even present on my keyboard.

One answer is to use ``raspi-config``.

I still need to dig to find a way to do this from the command line.