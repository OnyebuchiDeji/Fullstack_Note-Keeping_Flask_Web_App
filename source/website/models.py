"""
    Contains the database models.

    Continued: Sat-18-May-2024

"""

##  From current directory/package `.` import DB
from . import DB
"""
    The UserMixing is a custom class that can be inherited from to
    give the user object some things specific to the flask login.
    flask login is a module that helps one log users in.
    The user object should inherit this.

    Ken this:
    A database model is a blueprint/layout/template for an object that will be stored in
    one's database.

    This demonstrates a One-to-Many relationship between Users and their Notes
"""
from flask_login import UserMixin

"""
    This imports `func` so that the date field is not specified ourself but automatically
    by sql.
    Whenever a new node is created, it will automatically add the date to it.
    `func` gets the current date and time. It also returns the time zone information.
"""
from sqlalchemy.sql import func

class Note(DB.Model):
    """
        The ids are automatically assinged to every object created by the DB
    """
    id = DB.Column(DB.Integer, primary_key=True)
    data = DB.Column(DB.String(10000))
    ##  This stores the time zone information
    date_time = DB.Column(DB.DateTime(timezone=True), default=func.now())

    """
        Making a foreign key. A unique value that references a unique object in another table (the foreign object).
        Linking the Note object to a particular user.
        In this case, every Note object has a User that it belongs to.
        The foreign key identifies this relationship.
        And since one user can have many notes, it is a One-to-Many relationship.
        This foreign key enforces that a valid id from another object is given to create this Note object
        otherwise it will not be created.
    """
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'))


class User(DB.Model, UserMixin):
    """
        Here are the columns of the table that identify the
        data.
        This is a schema, a layout for the object to be stored inthe database. 
    """
    ##  Adding primary key here
    id = DB.Column(DB.Integer, primary_key=True)
    ##  The unique parameter makes it invalid to create a user whose email already exists
    email = DB.Column(DB.String(150), unique=True)
    password = DB.Column(DB.String(150))
    first_name = DB.Column(DB.String(150))
    """
        The below is for users to be able to find all of their notes.
        This tells sql that anytime a Note is created, add it to the current user's
        note's relationship, that Note object instance id.

        Note that a relationship references the name of the class Database model.
    """
    notes = DB.relationship("Note")
