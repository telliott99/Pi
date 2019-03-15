#### Flask

In this section of my Raspberry Pi pages, I want to explore [**Flask**](http://flask.pocoo.org).  

There is a Raspberry Pi tutorial on Flask [here](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask), but I am going to start with my old notes.

I worked with Flask a year ago (and another time before that), but it's scattered across several Github projects and not well organized.

#### The plan

The plan this time is to have projects numbered sequentially, and at least at first, to use the previous project as the basis for the next one.  So it's quite literally one step at a time.  

#### Preliminary

Flask is a web "framework" which is installed together with a web server like [gunicorn](https://gunicorn.org).

The version of Stretch Lite that I have comes with Python 3.5.  It doesn't have pip so

```
sudo apt-get update
sudo apt-get install python3-pip
```

and then

```
pip3 install flask
```

#### basic setup and config

- app in a [single file](one-file/README.md)
- [dynamic url](dynamic-url/README.md)
- standard app [skeleton](skeleton/README.md)
- using [proper html](html/README.md)
- simple [configuration](config-revised/README.md)
- [configuration](config/README.md)
- Pi [runs Flask](ports/README.md) on LAN

<hr>

#### forms

- [templates](templates/README.md)
- simple [button](button.md)
- [form](forms/README.md) example
- [CSRF token](csrf/README.md)

#### cookies, sessions and logins

- [cookie](cookie/README.md) example
- [session](session/README.md) cookie
- [login](login/README.md)


At this point, things have gotten pretty sophisticated.

