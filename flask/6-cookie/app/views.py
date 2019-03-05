from app import app
from flask import render_template
from flask import make_response, request

@app.route('/')
@app.route('/index')
def do_index():
    return render_template("form.html")

@app.route('/setcookie', methods = ['POST'])
def setcookie():
    print('request.form', request.form)
    if request.method == 'POST':
        user = request.form['nm']
        r = make_response(render_template(
            'clickme.html'))
        r.set_cookie('userID', user)
        return r
   
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'
