#### Note

Looking through some old code (scripter) I remembered an even simpler method for getting config info:

``config.py``

```
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
```

Just bare key-value pairs.  Unquoted keys.

And in ``__init__.py``:

```
app.config.from_object('config')
```

It works.  Terminal says:

```
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

After doing ``curl localhost:5000`` in another window, the Terminal window prints

```
True
127.0.0.1 - - [05/Mar/2019 15:14:10] "GET / HTTP/1.1" 200 -
```

because of this call in ``view.py``:

```
print(app.config['CSRF_ENABLED'])  # prints True
```