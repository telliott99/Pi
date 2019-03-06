from app import app
from flask import render_template, request
from flask import redirect, url_for
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    vL = [DataRequired()]
    name = StringField(
        'username',
        validators = vL)

#-----------------------------------

@app.route('/', methods= ['GET','POST'])
@app.route('/index', methods= ['GET','POST'])
def do_index():
    form = NameForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('time'))
        else:
            print('not validated', form.data)
    
    # either GET
    # or POST with failed validation
    return render_template(
        'hello.html', 
        form = form)

#-----------------------------------

@app.route('/time')
def time():
    s = "%A, %d %b %Y %l:%M %p"
    the_time = datetime.now().strftime(s)
    return render_template(
        'time.html', 
        time=the_time)    

