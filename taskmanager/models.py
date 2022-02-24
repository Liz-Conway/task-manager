'''
Created on 22 Feb 2022

Class-based models using SQLAlchemy's ORM

@author: fintan
'''
from taskmanager import db
# db has been defined as an instance of SQLAlchemy in '__init__.py'

# Each table needs a unique id acting as the Primary Key 
# - will auto-increment each new record added to the table
class Category(db.Model):
    # Schema for the Category model (table)
    # Instead of importing the datatypes (Integer, Float, etc.)
    # with SQLAlchemy the db import contains the datatypes
    # so we do not need to import them individually
    id = db.Column(db.Integer, primary_key=True)
    
    # Text column with max size of 25 characters
    # Ensure each new Category is unique
    # Make sure it is not empty or blank
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    
    '''
    In order to properly link our foreign key and cascade deletion, we need to add one more field to the Category table.
    We'll call this variable 'tasks' plural, not to be confused with the main Task class, 
    and for this one, we need to use db.relationship instead of db.Column.
    Since we aren't using db.Column, this will not be visible on the database itself like the other columns, 
    as it's just to reference the one-to-many relationship.
    To link them, we need to specify which table is being targeted, which is "Task" in quotes.
    Then, we need to use something called 'backref' which establishes a bidirectional relationship
    in this one-to-many connection, meaning it sort of reverses and becomes many-to-one.
    It needs to back-reference itself, but in quotes and lowercase, so backref="category".
    Also, it needs to have the 'cascade' parameter set to 'all, delete' 
    which means it will find all related tasks and delete them when a category is deleted.
    The last parameter here is lazy=True, which means that when we query the database for categories, 
    it can simultaneously identify any task linked to the categories.
    '''
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    
    # For each model we need to define this special method
    # Represent the class object as a String
    def __repr__(self):
        return self.category_name
    
class Task(db.Model):
    # Schema for the Task model (table)
    id = db.Column(db.Integer, primary_key=True)
    
    # Text column with max size of 50 characters
    # Ensure each new Category is unique
    # Make sure it is not empty or blank
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    
    # Text datatype allows longer Strings to be used
    task_description = db.Column(db.Text, nullable=False)
    
    # Boolean field
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    
    # Date datatype, could use Time or DateTime to include time
    due_date = db.Column(db.Date, nullable=False)
    
    # Foreign Key pointing to the specific Category for this Task
    # Need the ForeignKey() method so our database recognizes the relationship between our tables
    # Need to tell ForeignKey() which table and column to point to E.G. category.id
    # One-to-Many relationship, One Category can be applied to Many Tasks
    # Thus if we delete a Category we need to delete the corresponding Tasks
    category_id = db.Column(db.Integer, 
                    db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    
    # For each model we need to define this special method
    # Represent the class object as a String
    def __repr__(self):
        return "#{0} - Task : {1} | Urgent : {2}".format(
            self.id, self.task_name, self.is_urgent
        )

    
    
    