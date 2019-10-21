from flask import Flask, escape
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>index home</h1>"
