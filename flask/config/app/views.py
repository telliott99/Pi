from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def do_index():
    return render_template("index.html")
