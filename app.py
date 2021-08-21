from flask import Flask
# create app
app = Flask(__name__)

# create app route
@app.route('/')

def hello_world():
    return 'Hello world'

