#### html

We'll be serving a lot of HTML using Flask, so it's time to have some *real* html and not just that Python string 

```
<h1>Hello, world!</h1>
```

which, by the way, since markdown format accepts html tags, is:

<h1>Hello, world!</h1>

Here is a proper HTML page:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
  </head>
  <body>
    <h1><h1>Hello, world!</h1></h1>
  </body>
</html>
```

HTML is a dark art.  We will be moving on to real templates soon, so let's just leave it there.

If you want to know more, you could look at [Mark Pilgrim's book](https://diveintohtml5.info/index.html).

Put this file in ``templates`` as ``index.html``.

We must also modify ``views.py`` to use ``render_template``:

```
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def do_index():
    return render_template("index.html")
```

``cd`` into the project directory and test it with:

``` 
python3 app.py
```

Point Safari at ``localhost:5000`` and the result is just as before.

