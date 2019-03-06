from flask import render_template, url_for

from app import app

script_list = ['demo',
               'format_DNA',
               'translate',
               'extra_sites']
               
default_choice = 'format_DNA'

def render_index_template():
    return render_template(
        "index.html",
        script_list = script_list,
        default=default_choice)          

# index shows form with scripts listed
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_index_template()
