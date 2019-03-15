from app import app
from flask import render_template, request

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/dispatch', methods = ['GET','POST'])
def do_form():
    #print(dir(request))
    print(request.data)
    print(len(list(request.form.keys())))
    value = request.form["button"]
    print("button", value)
    
    return render_template(
        "info.html", 
        choice=value)
