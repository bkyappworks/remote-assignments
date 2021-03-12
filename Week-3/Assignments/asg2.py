# -*- coding: utf-8 -*-
import json
from flask import Flask, request, render_template, redirect, url_for, make_response
app = Flask(__name__)

#Assignment 1
@app.route('/')
def hello():
   return 'Hello, My Server!'
#Assignment 2

@app.route('/getData/')
def add(number = ""):
   number = request.args.get('number',number)
   if number == "":
      return "Lack of Parameter" 
   try:
      total = 0
      number = int(number)
      for i in range(number+1):
         total += i
      context = {'number':number,'total':total}
      return render_template("add.html",**context)
   except ValueError as err:
      return "Wrong Parameter"
 
app.run(debug = True,port = 3000, host = '0.0.0.0')

