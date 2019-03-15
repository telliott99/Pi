#### Skeleton of a project

In the first example [here](../one-file/README.md), we saw how little code is needed to have a Flask-based web-server.  

It can all be in a *single file*.  

The first ``app.py`` was

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def do_index():
    return "<h1>Hello, world!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

An object of the Flask class is our application.  It gets passed ``__name__`` to tell flask where to look for files.

It is run, of course, with ``app.run()``


A more usual organization is a project folder with:

```
app.py
app
  __init__.py
  views.py
  static
    < png files >
    < txt files >
  templates
    < index.html >
```

At the top-level, all you see is the ``app.py`` file and a folder named ``app``.  

The ``app`` folder contains ``__init__.py``, so it can be imported with the statement ``import app``.

We run ``python3 skeleton/app.py`` and then inside ``app.py`` do ``import app`` (the name duplication isn't a problem).  

That leads to the ``app`` folder and

**``__init__.py``**:

```
from flask import Flask
app = Flask(__name__)
from app import views
```

So there's the name ``app`` used for the third time:

```
app = Flask(__name__)
``` 

And I skipped over the fact that in ``app.py``, we actually do ``from app import app``. 

It's confusing, but with this statement we are asking ``app/__init__.py`` to provide us with the ``app`` object that is the result of ``Flask(__name__)``.

And since ``__init__.py`` is not ``__main``, i.e. not the first file processed by ``python3``, ``__name__`` is different.  

A ``print`` statement reveals that it is ``app
``.  This is really a fourth use of the same name.

#### ``app.py``

is actually simpler now:  three lines.

```
from flask import Flask
from app import app

app.run(debug=True)
``` 

We factor the routes out into ``views.py`` (sometimes I call it ``routes.py``):

**``views.py``**

```
from app import app

@app.route('/')
@app.route('/index')
def do_index():
    return "<h1>Hello, world!</h1>"
```

The import is needed so that ``views.py`` knows about the ``app`` object obtained from ``app = Flask(__name__)``.

Do ``python3 skeleton/app.py`` and point Safari at ``localhost:5000`` and you'll get Hello World, as before.

Stop the server with ``^C``, ``CTRL + C``.