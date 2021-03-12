import json
from flask import Flask, request, render_template, redirect, url_for, make_response, send_from_directory


app = Flask(__name__)

@app.route('/')
def test():
   return render_template("test.html")

@app.route('/getData/')
def index():
   return render_template("sum.html")

if __name__ == '__main__':
   app.run(debug = True, port = 3000, host = '0.0.0.0')



