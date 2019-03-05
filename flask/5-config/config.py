import os

class Config(object):
    k = os.environ.get('PORT')
    PORT = k or 5000
    if k:
        HOST = "0.0.0.0"
    else:
        HOST = "localhost"
        