#### Setting up Stretch-Lite for WiFi and ssh

Recall that for the Stretch desktop we first do this on the Pi:

```
Raspberry > Preferences > Configuration
```

- set Locale and Country Code
- toggle SSH service.  
- click on the WiFi icon
- click on a network, supply password.  
- reboot.

For Stretch-Lite, one can boot from the USB drive, login and then run the ``raspi-config`` tool (no "b" in the name) by doing ``sudo raspi-config``.

It gives a primitive GUI which you move around in by tabs and arrows and returns.  

I think it's a pain.

#### A better way

On the Mac I have this file

[**wpa_supplicant.conf**](../named_files/wpa_supplicant.conf)

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="Apple Network e7d46b"
    psk="<pw>"
    key_mgmt=WPA-PSK
}
```

Substitute the correct password.  Then, save ``wpa_supplicant.conf`` to the Desktop.

Now, having "burned" the .img file to the USB drive, it is no longer a .img file, but just a regular disk with two partitions.

However, the Mac doesn't read the file system ext4, so it sees only one partition, which is the FAT32 partition of the drive, with the ``/boot`` files, and it's mounted in ``/Volumes/boot``.  

We can write to it:

```
> touch /Volumes/boot/ssh
> cp ~/Desktop/wpa_supplicant.conf /Volumes/boot/wpa_supplicant.conf
> sudo diskutil eject /dev/disk2
```

Transfer the USB drive to the Pi and boot the Pi from it.  When finished, the Pi should be available over ssh.  

On the <i>Mac</i>:

```
ssh pi@10.0.1.7
```

If you see this error

```
Host key verification failed.
```

Delete ``10.0.1.7`` from ``~/.ssh/known_hosts`` on the Mac.

The login password is ``raspberry``.  It works:

```
pi@raspberrypi:~ $
```