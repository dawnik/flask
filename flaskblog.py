from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about')
def index():
    return render_template('about.html')