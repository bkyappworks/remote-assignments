#Assignment 4
import json
from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('bear'))
    except TypeError:
        data = {}
    return data #should be a python dict

@app.route('/trackName')
def index():
    data = get_saved_data()
    return render_template('index.html',saves = data)

@app.route('/save', methods=['POST'])
def save(): #set cookie here
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('bear', json.dumps(data))
    return  response # after subit, redirect to index


"""
def get_saved_data():
    try:
        data = json.loads(request.cookies.get('name'))
    except TypeError:
        data = {}
    return data


@app.route('/trackName')
def index():
   data = get_saved_data()
   return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
    )

@app.route('/save', methods=['GET','POST'])
def save(name = ""):
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('name', json.dumps(data))
    return response
"""
app.run(debug = True,port = 3000, host = '0.0.0.0')