'''
Created on 21 Feb 2022

@author: fintan
'''
from flask import render_template
from taskmanager import app, db


# Simple route using root directory
# Target a function called 'home()' which returns the rendered template of "base.html"
@app.route("/")
def home():
    return render_template("base.html")