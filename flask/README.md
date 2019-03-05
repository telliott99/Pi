#### Flask

In this section of the Raspberry Pi pages, I want to explore [**Flask**](http://flask.pocoo.org).  

There is a Raspberry Pi tutorial on Flask [here](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask), but I am going to start with my old notes.

I worked with Flask a year ago (and another time before that), but it's scattered across several Github projects and not well organized.

#### the plan

The plan this time is to have projects numbered sequentially, and at least at first, to use the previous project as the basis for the next one.  So it's quite literally one step at a time.  

#### preliminary

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

#### basic examples

- [single pyfile](1-single-pyfile/README.md)
- [skeleton](2-skeleton/README.md)
- [proper html](3-html/README.md)
- [exposed on the LAN](4-ports/README.md)
- [configuration](5-config.README)