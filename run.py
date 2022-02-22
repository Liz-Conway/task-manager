'''
Created on 22 Feb 2022

Main controller which is used to run the entire application
At the root of our application - not part of the taskmanager package

@author: fintan
'''
import os   # Since need to use environment variables
from taskmanager import app
from email.mime import application

# Tell our app how and where to run the application
# Check that the 'name' class is equal to the default 'main' string, wrapped in double underscores.
# If it's a match, then we need to have our app running, which will take three arguments:
# 'host', 'port', and 'debug'.
if __name__ == "__main__":
    app.run(
        host = os.environ.get("HOST"),
        port = int(os.environ.get("PORT")),
        debug = os.environ.get("DEBUG")
    )