from app import app

app.run(debug=True, 
    port=app.config['PORT'],
    host=app.config['HOST']
)
 