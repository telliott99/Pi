We have the Pi booted with Stretch-Lite, 

The OS was previously modified to add ``ssh`` and ``wpa_supplicant.conf`` to ``/boot``, so we have WiFi working and can do ssh by password.  See [here](backup4.md).

Now, we want to use ``scp`` to copy over a script that can finish the setup, along with any needed files.

The project is in this directory as ``archive.tar.gz``, constructed by

```
tar -zcvf archive.tar.gz setup-pi
```

#### sshpass

So it's clear that we should be able to copy the ``sshd_config`` file to the right place, and of course, get my public key to the right place.

Is there a way to automatically deal with the password input?  

This allows us to write *another* script to bundle this stuff.  We want to issue **one** command on the Mac and have it all just go.

According to [this](https://stackoverflow.com/questions/12202587/automatically-enter-ssh-password-with-script) sshpass will do it.

Like so:

```
sshpass -p "YOUR_PASSWORD" ssh -o StrictHostKeyChecking=no YOUR_USERNAME@SOME_SITE.COM
```

I need it on the Mac.  Homebrew says:

```
Error: No available formula with the name "sshpass" 
We won't add sshpass because it makes it too easy for novice SSH users to
ruin SSH's security.
```

But here is a [gist](https://gist.github.com/arunoda/7790979) that explains how to trick Homebrew into installing it.

```
brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```

It needs to build anyway...

We do:

```
sshpass -p "raspberry" ssh -o StrictHostKeyChecking=no pi@10.0.1.7
```

It works!

#### Outline of the solution

```
setup-pi
|--do-scp
|--go
|--run-setup
|--tmp
   |--motd
   |--setup
   |--ssh_config.both
   |--ssh_config.ssh_only
```

When `setup-pi/go`` is run with printing enabled, we get:

```
> setup-pi/go
in go
after tar -c
in run-setup
in setup
ssh-rsa AAAAB3NzaC1y
PasswordAuthentication no
PubkeyAuthentication yes
exit go
>
```

So ``go`` looks like this:

```
#! /bin/bash

echo "in go"
cd setup-pi

cp ~/.ssh/id_rsa.pub tmp/key

tar -zcf tmp.tar.gz tmp
echo "after tar -c"

./do-scp
./run-setup

rm -r tmp.tar.gz
echo "exit go"
```

Since we launched from the Desktop, we must ``cd`` into ``setup-pi`` and then copy in my key.  We turn the subdirectory ``tmp`` into ``.tar.gz`` archive and then call ``do-scp`` and ``run-setup``.  At the end we clean up by deleting the archive file.

**``do-scp``**

```
#! /bin/bash

sshpass -p 'raspberry' scp tmp.tar.gz pi@10.0.1.7:~
```

is a simple script that copies the archive to the Pi.  The magic is that ``sshpass`` handles the password authentication for us.

I separated out some of the logic into 

**``run-setup``**

```
#! /bin/bash

echo "in run-setup"

# silence tar -x warning about timestamp
sleep 2

sshpass -p "raspberry" \
ssh -o StrictHostKeyChecking=no pi@10.0.1.7 \
'tar -zxf tmp.tar.gz;\
tmp/setup; rm -r tmp*'
```

The above does ``ssh`` into the Pi and then we are running the rest of the commands on the Pi. So that's why the big one-liner, that has to run from the Mac before we get to the Pi.

Unpack the archive file and run the ``setup`` script that is inside.  At the end, we clean up.

So now, we are on the Pi

**``setup``**

```
#! /bin/bash
echo "in setup"

cd tmp
#echo "in tmp"
#ls -al key*

mkdir ~/.ssh
#ls -al ~

cp key ~/.ssh/authorized_keys
sudo chown pi:pi ~/.ssh/authorized_keys

sudo cp motd /etc/motd

#echo "after copy"
#echo "ls ssh"
#ls -al ~/.ssh
#pwd
#ls -al .

sudo cp sshd_config.ssh_only /etc/ssh/sshd_config

cd ~
#echo "key"
cat ~/.ssh/authorized_keys | cut -c 1-20
sudo cat /etc/ssh/sshd_config | grep "Password" | head -n 1
sudo cat /etc/ssh/sshd_config | grep "Pubkey"

#echo "exit script"
```

We ``mkdir`` the ``.ssh`` directory.  For some reason, its owned by root.

opy the key into ``authorized_keys``, copy over ``motd`` and the ``sshd_config`` file to the final locations.

Then just ``cat`` some of the files to show they are correct.

I used the configuration file ``ssh_config.both`` until I was sure it all worked.

#### Important

It's important to keep a separate Terminal windown on the Mac that remains logged into the Pi in case something goes wrong.

So even when I test at the end, I lauch a *new* Terminal window and do 

```
> ssh pi@10.0.1.7
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

Peace and love.
Last login: Sat Feb 23 19:23:05 2019 from 10.0.1.4
pi@raspberrypi:~
```

I actually did screw up and have to copy a file over to the Pi by plugging my USB drive into it.

Insert the drive and then to mount the drive on the Pi

```
sudo mkdir /mnt/usb
sudo mount /dev/sdb1 /mnt/usb
sudo cp /mnt/usb/<filename> /home/pi
```

I had to do ``/home/pi`` because the ``~`` key doesn't work!

#### Quick Test in 3 min

On the Mac:

```
hdiutil attach os.img
sudo dd bs=1m if=os.img of=/dev/rdisk2 conv=sync
diskutil eject /dev/disk2
```
Two minutes for the copy.  Insert the micro SD card into the Pi and power up.

Still on the Mac:

```
tar -zxvf ~/Dropbox/Github/raspberrypi/disk-stuff/archive.tar.gz setup-pi
setup-pi/go
```

and

```
> ssh pi@10.0.1.7
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

Peace and love.
Last login: Sat Feb 23 21:14:25 2019 from 10.0.1.4
pi@raspberrypi:~ $
```