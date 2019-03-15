#### Note

Last time we talked about a ``Config`` class, but there is an even simpler method for getting config info:

**``config.py``**

```
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
PORT = 8000
HOST = "0.0.0.0"
```

Just put bare key-value pairs in the config file, with unquoted keys and ints, strings or booleans as values.

**``__init__.py``**:

```
app.config.from_object('config')
```

It works.  

Terminal says:

```
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Because of this call in ``view.py``:

```
print(app.config['CSRF_ENABLED'])  # prints True
```
After doing ``curl localhost:8000`` in another window, the Terminal window prints

```
True
127.0.0.1 - - [05/Mar/2019 15:14:10] "GET / HTTP/1.1" 200 -
```
