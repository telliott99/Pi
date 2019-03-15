from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def do_index():
    print(app.config['CSRF_ENABLED'])  # prints True
    return render_template("index.html")
