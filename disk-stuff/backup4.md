For configuration we need to:

- set Locale and Country Code
- turn on WiFi and set the password
- turn on SSH service
- provide a public key for the user's login
- turn on Pubkey Authorization 

I have a modified image of the Lite OS that works for all of that when booted on a USB drive.

Now we try the same image on an SD card.

#### SD card

I got a USB [card reader]().  The micro slot doesn't work, but a micro card works with an adapter.

Burn the backup-mod.img to the card (exactly like with the USB drive).

Then boot the Pi from the micro SD card.  

Remove 10.0.1.7 from known_hosts and try ssh.  It fails:

```
> ssh pi@10.0.1.7
The authenticity of host '10.0.1.7 (10.0.1.7)' can't be established.
ECDSA key fingerprint is SHA256:R6eMmjKuVHwV1d6BiLFyQ5EdLT0l+Q4M87QNDwOh3bE.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.0.1.7' (ECDSA) to the list of known hosts.
p
```

Login from the Terminal.  Look in ``~/.ssh/authorized_keys``.  Nothing

What's goin on is that ``~/.ssh`` is now owned by ``root``.

Furthermore, I can't login with password b/c the changed file *is* in ``/etc/sshd_config``.

I can't see all of it b/c the key mappings are wrong, so I can't find the `|`.  `|` on the keyboard gives `~`.  Weird...

So I have an image, ``backup-mod.img``, which, when copied to a USB drive, works to boot the Pi and it behaves as expected.  But when copied to an SD card, it doesn't work correctly.  Pretty strange!

``/etc/default/keyboard`` shows ``XKBLAYOUT="gb"`` which isn't so surprising.

Ohhhhhh.....

``raspi-conf`` shows that neither the Locale nor WiFi is set up.

The ``wpa_supplicant.conf`` stuff is not being executed from the SD card, but it is from USB!  

So I can't make backups to cards, it looks like.

