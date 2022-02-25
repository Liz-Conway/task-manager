'''
Created on 21 Feb 2022

The entire application will need to be its own Python package, 
so to make this a package, we need a new folder which we will simply call taskmanager/.
Inside of that, a new file called __init__.py
This will make sure to initialize our taskmanager application as a package, 
allowing us to use our own imports, as well as any standard imports.

@author: fintan
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
'''
In order to actually use any of our hidden environment variables, we need to import the 'env' package.
However, since we are not pushing the env.py file to GitHub, 
this file will not be visible once deployed to Heroku, and will throw an error.
This is why we need to only import 'env' if the OS can find an existing file path for the env.py file itself.
'''
if os.path.exists("env.py"):
    import env  # noqa
# noqa means 'no quality assurance' - the linter will not try to validate this line

# Create an instance of the imported Flask class
# takes the default Flask 'name' module
app = Flask(__name__)

# Specify app configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# If we are working on our local PC
if os.environ.get("DEVELOPMENT") == True:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
# Otherwise we are running the application in Heroku
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# Create an instance of the imported SQLAlchemy class
# Set to the instance of our Flask 'app'
db = SQLAlchemy(app)

# routes file will depend on both app and db variables declared above
from taskmanager import routes # noqa

