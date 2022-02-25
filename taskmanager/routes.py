'''
Created on 21 Feb 2022

@author: fintan
'''
from flask import render_template, request, redirect, url_for
from taskmanager import app, db

# Need to manually create the database
# But the tables will be automatically generated
# Need to import model classes in order to generate the db schema in Postgres
from taskmanager.models import Task, Category
from _blueman import page_timeout

# Simple route using root directory
# Target a function called 'home()' which returns the rendered template of "base.html"
@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    # Retrieve all categories from the DB
    # categoriesVar = Category.query.all()   # Automatically sorts by the primary key
    # The next line returns a Cursor object
    # categoriesVar = Category.query.order_by(Category.category_name).all()
    
    # Store the categories as an ordinary array/list
    categoriesVar = list(Category.query.order_by(Category.category_name).all())
    
    # Pass the categories from the DB into the HTML template
    return render_template("categories.html", categories = categoriesVar)

'''Need to add GET and POST methods since we will be
submitting a form to the DB
GET = When the user clicks a link to the 'Add Category' page
POST when the user submits the form'''
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # Create a Category ORM object, setting the name to the name added in the form
        category = Category(category_name = request.form.get("category_name"))
        # Add the form data to the database
        db.session.add(category)
        db.session.commit()
        '''Run the categories() method to show the 'Categories' page
        after submitting the new category'''
        return redirect(url_for("categories"))
    
    return render_template("add_category.html")

'''Passing parameters into our Controller functions
   must be wrapped in angle brackets and cast to the appropriate datatype
   We must also pass it as a parameter to the method'''
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    '''get_or_404() -  Queries the database and attempts to find the specified record 
    using the data provided, and if no match is found, it will trigger a 404 error page.'''
    categoryObj = Category.query.get_or_404(category_id)
    
    if request.method == "POST":
        categoryObj.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    
    return render_template("edit_category.html", category=categoryObj)    # GET method

'''Passing parameters into our Controller functions
   must be wrapped in angle brackets and cast to the appropriate datatype
   We must also pass it as a parameter to the method'''
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    '''get_or_404() -  Queries the database and attempts to find the specified record 
    using the data provided, and if no match is found, it will trigger a 404 error page.'''
    categoryObj = Category.query.get_or_404(category_id)
    
    db.session.delete(categoryObj)
    db.session.commit()
    
    return redirect(url_for("categories"))
