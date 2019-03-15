from flask import Flask, session, redirect
from flask import url_for, escape, request, render_template

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
@app.route('/index')
def index():
    print('index')
    for c in request.cookies:
        print(c)
    print('-----')
    if 'username' in session:
        username = session['username']
        r = '''
            You are logged in as %s <br>
            <b><a href = '/logout'>
            click here to log out</a></b>
            '''
        return r % username       
          
    r = '''
        You are not logged in 
        <br><a href='/login'></b>
        click here to log in</b></a>
        '''
    return r

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
       
    r = '''
        <form action="/login" method="post">
        <p> <input type='text' name=username> </p>
        <p> <input type='submit' value='Login'/> </p>
        </form>
        '''
    return r
   
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)