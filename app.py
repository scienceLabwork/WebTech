from flask import Flask, render_template, request, redirect
import time
import os

app = Flask(__name__,static_url_path='', static_folder='frontend/static',template_folder='frontend/templates')
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lab3')
def lab3():
    return render_template('lab3.html')

@app.route('/lab2B')
def lab2b():
    return render_template('lab2B.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)