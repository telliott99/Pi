import os

k = os.environ.get('SECRET_KEY')
SECRET_KEY = k or 'you-will-never-guess'

SESSION_KEY = str(os.urandom(24))
    
k = os.environ.get('RUN_FLASK_DEBUG')
DEBUG = k or False

