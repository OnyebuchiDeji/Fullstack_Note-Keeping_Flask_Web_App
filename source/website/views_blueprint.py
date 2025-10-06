"""
    Making this file a blueprint.
    1. Houses the home route
    2. Renders home_page.html. Here it takes some arguments
        which are accessed by the HTML template using Jinja language
    3. This is where the request to create a note from the home_page form
       is handled.
       Notes are created and added to the database, for the appropriate user
    4. Implemented the button for deleting notes.
        The button sends a POST request to the endpint, delete_note
"""

from . models import Note
from . import DB
from flask import Blueprint, render_template, request, flash, jsonify
##  Current User to detect whether the current user is logged in or not
##  With it all information about the current User -- name, email, notes
##  If no user is signed in, the current User will be anonymous 
from flask_login import login_required, current_user
import json

views = Blueprint('views', __name__)




##  Home Page's route
@views.route('/', methods=["GET", "POST"])
@login_required ##  So one cannot get to homepage unless they login
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short.", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            DB.session.add(new_note)
            DB.session.commit()
            flash("Note Added!", category="success")
    ##  With the user keyword, the current user can be accessed by the html template
    ##  to check if there is a current user. If there is a current user, their name us displayed.
    return render_template("home_page.html", text="Test Passed Argument", author="Deji", user=current_user)


@views.route("/delete_note", methods=["POST"])
def delete_note():
    """
        Because the request is not sent as a form, the request comes in
        with the `data` parameter of the request object.
        Hence it needs to be loaded as JSON.
        The JSON is sent as a JSON string.
    """
    note_data  = json.loads(request.data)
    ##  Access noteId value from key-value string
    noteId = note_data['noteId']
    ##  Get this note from the database
    existing_note = Note.query.get(noteId)
    ##  If the note exists
    if existing_note:
        if existing_note.user_id == current_user.id:
            DB.session.delete(existing_note)
            DB.session.commit()
            flash("Note Deleted.")
    ##  Return an empty json dictionary
    return jsonify({})