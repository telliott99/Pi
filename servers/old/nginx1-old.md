#### Configure nginx

[**nginx**](http://nginx.org/en/) is another popular server.  

- [Overview](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations) comparing Apache and nginx
- Pi [docs](https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md)
- [TTutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-14-04-lts) at Digital Ocean

nginx is installed on the Stretch desktop, see [here](../files/21.md), and is up and running.

It was not running on Stretch Lite

```
> ps -A | grep "nginx"
 1735 ttys000    0:00.00 grep nginx
```

An easy way to check if it's installed is just to try installing it:

```
sudo apt-get update
sudo apt-get install nginx -u
```

which then installs it.  (Or you could [build](https://www.bitpi.co/2015/08/04/how-to-set-up-an-nginx-server-on-a-raspberry-pi/) it).


The service is up automatically

```
pi@raspberrypi:~ $ ps -A | grep "nginx"
15031 ?        00:00:00 nginx
15032 ?        00:00:00 nginx
15033 ?        00:00:00 nginx
15034 ?        00:00:00 nginx
15035 ?        00:00:00 nginx
```

```
pi@raspberrypi:~ $ curl localhost
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
```

If it had been necessary to start it

```pi@raspberrypi:~ $ sudo /etc/init.d/nginx start
[ ok ] Starting nginx (via systemctl): nginx.service.
```

To automatically run on boot it may be necessary to do:

```
sudo update-rc.d -f nginx defaults
```

The ``-f`` (force) flag forces removal of some sym links (see the manual)

From the Mac by ssh

```
> curl 10.0.1.7
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
```

The default set-up works.

#### Setting up the host

In ``/etc`` we find ``/etc/hostname``, which contains ``raspberrypi``.

At least from the Pi, our ``localhost`` ip address, ``127.0.0.1`` is reachable as ``raspberrypi``.  (On the LAN it is raspberry.local).

We want to add another domain name.

Just edit ``/etc/hosts`` to add ``test.com``.  After the edit:

```
pi@raspberrypi:~ $ cat /etc/hosts
pi@raspberrypi:~ $ cat /etc/hosts
127.0.0.1   localhost
::1         localhost ip6-localhost ip6-loopback
ff02::1     ip6-allnodes
ff02::2     ip6-allrouters

127.0.1.1   raspberrypi
127.0.1.2   test.com
pi@raspberrypi:~ $ curl test.com
<!DOCTYPE html>
```

According to [wikipedia](https://en.wikipedia.org/wiki/Hosts_(file)#File_content)

> tabs are often preferred for historical reasons, but spaces are also used

The default file has a mix of single and double tabs.  I don't like tabs (a legacy of using Python), so I converted to spaces.

The people who set up the Pi OS *really* want you to use nano.  Or you can 


One could also do ``sudo echo "127.0.1.2       test.com" >> /etc/hosts``.

(If, while editing with nano, you forget to ``sudo``, it won't let you save.  In that case, you can save to the Desktop or home and then ``sudo mv hosts /etc/hosts`` will work).

The people who set up the Pi OS *really* want you to use nano.  Or you can copy to the Pi's Desktop, do ``echo "127.0.1.2 test.com" >> hosts`` and then copy back to ``/etc``.  Or you can do as I do and scp over to the Mac and edit there and then on the Mac

```
> scp hosts pi@10.0.1.7:~
```

and on the Pi:

```
 sudo mv hosts /etc/hosts
```

This should now work:

```
pi@raspberrypi:~ $ curl test.com
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
```
#### Modify sites-enabled

The way this works is that in ``/etc/nginx/sites-enabled`` there is a sym link

```
lrwxrwxrwx 1 root root   34 Feb 28 14:18 default -> /etc/nginx/sites-available/default
```

which says for the default server nginx should  go to the file in ``/etc/nginx/sites-available/default`` and read it.

The default **server block** directives specifies the server to look for documents in ``/usr/share/nginx/html`` (the default index page is found in ``/usr/share/nginx/html/index.html``)

To edit it (once again I copy it to the Mac):

```
> scp pi@10.0.1.7:/etc/nginx/sites-available/default default
```

I remove the ``#`` comment symbols from the example (and don't bother about the tabs), change "example" to "test", and save as ``test.com``.

```
server {
	listen 80;
	listen [::]:80;

	server_name test.com;

	root /var/www/test.com;
	index index.html;

	location / {
		try_files $uri $uri/ =404;
	}
}
```

Let's first see if we can make this work as is before editing it.  

We can't copy directly to the target directory so first from the Mac

```
> scp test.com pi@10.0.1.7:~
```

and then on the Pi

```
$ sudo mv ~/test.com /etc/nginx/sites-available
```

and then make a sym link to it

```
$ cd /etc/nginx
$ $ sudo ln -s sites-available/test.com sites-enabled/test.com
```

The *existing* file comes first, then the link name comes second.

```
pi@raspberrypi:~ $ curl test.com
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
```

Since the default config is still present, I'm not absolutely sure this is working as we think it is.  But first, let's modify the document root.

#### Modify the document root

Suppose we want to use ``www/var`` since that is more usual.  

First, set up the directories:

```
sudo mkdir -p /var/www/test.com/html
```

The ``-p`` flag with ``mkdir`` "creates intermediate directories as required."

Make sure permissions are good:

```
pi@raspberrypi:~ $ ls -al /var/www/test.com/html
total 8
drwxr-xr-x 2 root root 4096 Feb 20 12:25 .
drwxr-xr-x 3 root root 4096 Feb 20 12:25 ..
```

The main thing is that the permissions look fine (755), but I should be the owner. 

The suggested method

```
sudo chown -R $USER:$USER /var/www
``` 

Construct a custom index page:

**index.html**

```
<html>
  <head>
    <title>Welcome to test.com!</title>
  </head>
  <body>
    <h1>Success!  The test.com server block is working!</h1>
  </body>
</html>
```

Copy it over

```
> scp index.html pi@10.0.1.7:~/index.html
index.html            100%  157    37.5KB/s   00:00    
```

```
pi@raspberrypi:~ $ sudo mv ~/index.html /var/www/test.com/html
```

Just check

```
pi@raspberrypi:~ $ ls -al /var/www
total 16
drwxr-xr-x  4 pi   pi   4096 Feb 28 14:53 .
drwxr-xr-x 12 root root 4096 Feb 28 14:18 ..
drwxr-xr-x  2 pi   pi   4096 Feb 28 14:18 html
drwxr-xr-x  3 pi   pi   4096 Feb 28 14:53 test.com
```

Recall that we modified this file already:

```
/etc/nginx/sites-available/test.com
```

Restart the server

```
sudo service nginx restart
```


and test:

```
pi@raspberrypi:~ $ curl test.com
curl: (7) Failed to connect to test.com port 80: Connection refused
```

Check the log:

```
cat /var/log/nginx/error.log | tail -n 5
```

Hmm..  Well, there is still a sym link in ``sites-enabled``,  so delete it.












What we need for the *server block* is ``root /var/www/test.com;``:

```
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/test.com;
    server_name test.com www.test.com;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

I paste just this text into ``x.txt`` and copy it back with ``scp``:

```
> scp x.txt pi@10.0.1.7:Desktop
x.txt                 100%  208    32.9KB/s   00:00    
```

and then

```
sudo cp x.txt /etc/nginx/sites-available/test.com
```

#### Server blocks: enable

```
sudo ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/
```

Disable the default server block:

```
pi@raspberrypi:~/Desktop $ sudo mkdir /etc/nginx/sites-enabled/old
pi@raspberrypi:~/Desktop $ sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/old
```
    
Edit ``/etc/nginx/nginx.conf`` with nano and uncomment the line 

``server_names_hash_bucket_size 64;`` and save, and then:

```
pi@raspberrypi:~/Desktop $ sudo service nginx restart
Job for nginx.service failed because the control process exited with error code.
See "systemctl status nginx.service" and "journalctl -xe" for details.
```

So it doesn't work.

#### Trouble-shooting

It's not working...  and the error messages don't help me.

What about indentation?  From [here](https://www.nginx.com/resources/wiki/start/topics/examples/coding_style/)

- K&R style indentation
- 4 space indentation, no tabs
- 2 line breaks between blocks at global level
- C style comments only

So, edit the tabs and try again.

Nope.

Try changing the owner of ``/var/www`` back to root.

Nope.

The problem was that I had made a directory ``/etc/nginx/sites-enabled/old`` and moved ``default`` there. 

I should have checked the nginx log:

```
pi@raspberrypi:~ $ cat /var/log/nginx/error.log
2019/02/27 11:09:31 [crit] 7822#7822: pread() "/etc/nginx/sites-enabled/old" failed (21: Is a directory)
```

Removing it 

```
sudo mv /etc/nginx/sites-enabled/tmp ~
```

and now

```
sudo service nginx restart
``` 

runs without error.  Then

```
pi@raspberrypi:~ $ curl test.com
<html>
<head><title>403 Forbidden</title></head>
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.10.3</center>
</body>
</html>
pi@raspberrypi:~ $
```

That's sorta right.  The server is giving us a page, it's just not the one we want.  It's a 403, access error.

``curl test.com/index.html`` gives a 404.

