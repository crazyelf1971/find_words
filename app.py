#!flask/bin/python
from flask import Flask
from flask import render_template
import datetime as dt

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World, hello! " + str(dt.datetime.now())

if __name__ == '__main__':
    app.run()
