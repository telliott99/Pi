https://stackoverflow.com/questions/49219192/atom-on-raspbian

clean install of Stretch w/Desktop

https://discuss.atom.io/t/atom-on-the-raspberry-pi/33332

pi@raspberrypi:~ $ sudo apt-get install build-essential git libgnome-keyring-dev fakeroot gconf2 gconf-service libgtk2.0-0 libudev1 libgcrypt20 python rpm npm npm-cli apm nodejs
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package npm-cli
E: Unable to locate package apm


https://www.npmjs.com/get-npm

npm is a package manager that comes with node

so apt-get install node

npm -v

https://github.com/atom/apm

apm is bundled and installed automatically with Atom.

apm bundles npm with it ...

pi@raspberrypi:~ $ sudo apt-get install node-js
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package node-js
