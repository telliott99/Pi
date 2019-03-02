TL;DR

- ``sudo update-rc.d apache2 enable/disable`` to control startup behavior
- ``/etc/init.d/apache2 start/stop`` to manually start/stop the service

#### Start/stop services

We tried several commands to start/stop apache2

- ``/etc/init.d/apache2 start/stop``
- ``sudo systemctl enable/disable apache2``
- ``sudo update-rc.d apache2 enable/disable``

What are ``init.d``, ``rc.d`` and ``systemctl``?

#### init.d and rc.d

- init.d contains start/stop scripts
- rc.d is not used on Debian (although traces remain)

[docs](https://askubuntu.com/questions/5039/what-is-the-difference-between-etc-init-and-etc-init-d/5042#5042)

> /etc/init.d contains scripts used by the System V init tools (SysVinit). This is the traditional service management package for Linux, containing the init program (the first process that is run when the kernel has finished initializing¹) as well as some infrastructure to start and stop services and configure them. Specifically, files in /etc/init.d are shell scripts that respond to start, stop, restart, and (when supported) reload commands to manage a particular service. These scripts can be invoked directly or (most commonly) via some other trigger (typically the presence of a symbolic link in /etc/rc?.d/).

rc stands for "run commands"

According to [this](https://unix.stackexchange.com/questions/3537/etc-rc-d-vs-etc-init-d/170965)

Debian and Ubuntu (based on Debian) use init.d not rc.d

/etc/init.d is simply a shell script that starts/stops the server.

#### update-rc.d

According to [this](https://www.debuntu.org/how-to-managing-services-with-update-rc-d/)

> Linux services can be started, stopped and reloaded with the use of scripts stocked in /etc/init.d/.

> However, during start up or when changing runlevel, those scripts are searched in /etc/rcX.d/ where X is the runlevel number.

> This tutorial will explain how one can activate, deactivate or modify a service start up.

> When installing a new service under debian, the default is to enable it. So for instance, if you just installed apache2 package, after you installed it, apache service will be started and so will it be upon the next reboots.

> If you do not use apache all the time, you might want to disable this service from starting up upon boot up and simply start it manually when you actually need it by running this command:

>  /etc/init.d/apache2 start
 
> You could either disable this service on boot up by removing any symbolic links in /etc/rcX.d/SYYapache2 or by using update-rc.d.

> The advantage of using update-rc.d is that it will take care of removing/adding any required links to /etc/init.d automatically.

So

- start/stop scripts in ``/etc/init.d/``
- example ``/etc/init.d/apache2 start``
- on startup search ``/etc/rcX.d/`` where X is the runlevel number
- on install of a service, default is to enable it
- ``update-rc.d`` enable/disables service on boot up
- some links are in /etc/rcX.d files

#### systemctl

The Pi [docs](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) have an example of a user-defined service.  We'll try that another time.

It seems that ``init.d`` is for distributed packages and the like (but see [this](https://debian-administration.org/article/28/Making_scripts_run_at_boot_time_with_Debian)).  

We should come back to both of these tutorials at another time.
