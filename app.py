from flask import Flask, render_template, request, redirect
import time
import os
import pandas as pd

app = Flask(__name__,static_url_path='', static_folder='frontend/static',template_folder='frontend/templates')
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/index')
def index():
    rf = "data.csv"
    df = pd.read_csv(rf)
    df = df.to_dict('records')
    print(df)
    l = []
    for i in range(len(df)):
        file = f"lab{df[i]['count']}.html"
        l.append(file)
    return render_template('index.html',data=df, lenr=len(df), uri=l)

@app.route('/<string:practical_id>')
def practical(practical_id):
    return render_template(practical_id)

@app.route('/l2a1')
def l2a1():
    return render_template('l2a1.html')

@app.route('/l2a2')
def l2a2():
    return render_template('l2a2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)