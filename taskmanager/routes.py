'''
Created on 21 Feb 2022

@author: fintan
'''
from flask import render_template
from taskmanager import app, db

# Need to manually create the database
# But the tables will be automatically generated
# Need to import model classes in order to generate the db schema in Postgres
from taskmanager.models import Task, Category

# Simple route using root directory
# Target a function called 'home()' which returns the rendered template of "base.html"
@app.route("/")
def home():
    return render_template("tasks.html")