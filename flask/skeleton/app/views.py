from app import app

@app.route('/')
@app.route('/index')
def do_index():
    return "<h1>Hello, world!</h1>"
