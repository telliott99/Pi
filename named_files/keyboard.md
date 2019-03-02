The bash shell has something called Tilde expansion.  If a word begins with ``~`` (unquoted), then if there's nothing else there the tilde is replaced with the value of the HOME shell variable.

So ``~ `` with a space is the same as $HOME.

It would have been handy the other day when struggling with a keyboard layout that didn't have ``~`` in the upper left.  (Although it turns out to be where ``|`` is).  And ``|`` maps to a key (left of ``z``) that isn't even present on my keyboard.

https://www2.physics.ox.ac.uk/it-services/how-to-type-the-sharp-key

I wasn't using the raspi-config tool correctly to specify my keyboard changes.  Remember:  TAB to advance between the list of selections -> Ok -> Cancel, Return or Enter to select, and arrows to navigate the list.

It is under

4 Localization
  I3 Keyboard Layout

I just chose Apple and English(US).

Now the keys work as expected.  At least the ones I tested.

Also:  CTRL+L clears the monitor (not K as on macOS).
