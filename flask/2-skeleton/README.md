#### Skeleton of a project

In the first example [here](../1-single-pyfile/README.md), we saw how little code is needed to have a Flask-based web-server.  

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

A more usual organization for a simple project is a project folder with:

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

The ``app`` folder contains ``__init.py``, so it can be imported.

We do ``python3 2-skeleton/app.py`` and then inside ``app.py`` do ``import app`` (the name duplication isn't a problem).  That leads us to the ``app`` folder and

**``__init__.py``**:

```
from flask import Flask
app = Flask(__name__)
from app import views
```

So here's the name ``app`` used for the third time:

```
app = Flask(__name__)
``` 

I skipped over the fact that in ``app.py``, we actually do ``from app import app``. 

It's confusing, but with this statement we are asking ``app/__init__.py`` to provide us with the ``app`` object that is the result of ``Flask(__name__)``.

And since ``__init__.py`` is not ``__main``, i.e. not the first file processed by ``python3``, ``__name__`` is different.  

A ``print`` statement reveals that it is ``app
``.  This is really a fourth use of the same name.  Makes your head spin.

#### ``app.py``

is actually simpler now. 

```
from flask import Flask
app = Flask(__name__)
app.run(debug=True)
``` 

We split the routes out into ``views.py``:

```
from app import app

@app.route('/')
@app.route('/index')
def do_index():
    return "<h1>Hello, world!</h1>"
```

This import is needed so that ``views.py`` knows about the ``app`` object obtained from ``app = Flask(__name__)``.

Do ``python3 2-skeleton/app.py`` and point Safari at ``localhost:5000`` and you'll get Hello World, as before.

Stop the server with ``^C``, ``CTRL + C``.