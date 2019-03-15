from app import app
from flask import render_template, request
from flask import redirect, url_for, session

from flask_wtf import FlaskForm

def get_count(session):
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 0
    return session['visits']

def do_form():
    form = FlaskForm()
    
    print('in do_form')
    print('session data:')
    for k in session:
        print(k, session[k])
    print(len(session.keys()), 'items in session')
    print('**')
    
    print('form data:')
    for k in form.data:
        if not form.data[k]:
            print('None')
        else:
            print(k, form.data[k][:35] + '..')
    print('*')

    template = 'click.html'
    count = get_count(session)
      
    plural = not (count == 1)
    if count == 0:
        count = "no"
    else:
        count = str(count)
        
    return render_template(
        template,
        form = form,
        count = count,
        plural = plural)

#-----------------------------------------

@app.route('/')
@app.route('/index')
def do_index():
    return do_form()
    
#-----------------------------------------

@app.route('/click', methods= ['GET','POST'])
def do_click():
    print('rdata: ')
    print(request.data)
    print('*')
    return do_form()
        
@app.route('/reset', methods= ['POST'])
def do_reset():
    session.pop('visits', None)
    return do_form()

