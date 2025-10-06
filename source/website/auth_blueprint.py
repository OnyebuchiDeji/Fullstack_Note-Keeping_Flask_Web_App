"""
    Making this file a blueprint.

    ##  Adding these endpoint, according to user authentication:
    1. Login
    2. Sign Up
    3. Logout

    4. ##  Added *message flashing*.
        Note that the flash messages need to be also written in the corresponding
        html template. 
    
    5. Added code to add user to the Database
    6. Added password hashing:
        Here are different hashing methods:
        a)  bcrypt: Used against brute-force attacks because of its security and resistance.
                    It's the default hashing method for werkzeug.
        b) pbkdf2_sha256: PBKDF2 with SHA-256 iteratively applies the SHA-256 hash function to the
                    input password; hence very much computationally expensive to brute-force
        c) sha256_Crypt: Based on the SHA-256 hash function -- uses salted hashing to enhance security.
"""     

from . import DB

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
"""The below encrypts a password so it's not in plain text"""
from werkzeug.security import generate_password_hash, check_password_hash

""" Current user represents the current user"""
from flask_login import login_user, login_required, logout_user, current_user

"""
    Hashing functions have no inverse.
    So f(x)->y
    but f`(y) !-> x
    Hashing functions take a password and give an encrypted text
    But if it takes that encrypted text, the original value cannot be found.
    It's a one-way function.
    So not even those on the server-side can check the passwords of users that enter.
    
    When a password is entered, it is hashed and its hashed value is saved.
    So when as user eneters that same password, and it is hashed...
    if the password matches the previously entered hashed password, then the user is true.
    Give them access to their account.
    Hashed passwords can never be turned back to the original password.


"""

auth = Blueprint('auth', __name__)


"""
    By default only GET requests can be gotten
"""
@auth.route("/login", methods=["GET", "POST"])
def login_page():
    """
        the object returned by request.form is an ImmutableMultiDict --
        immutable multi-dictionary.
        It can be gotten from a GET request when switching url endpoints
        or from POST when submitting form INFO
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        ##  Filter all of the users that have the matching email/
        ##  .first() returns the first result.
        ##  THere should be only one result since emails should be unique
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            ##  Match the found user's password with the password gotten
            ##  from login form
            if check_password_hash(existing_user.password, password):
                flash("Logged in successfully!", category="success")
                ##  This will login the user
                ##  remember=True stores a flask session. So as long as the flask server has not been restarted
                ##  the user can login awithout entering details.
                login_user(existing_user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password. Try again.", category="error")
        else:
            flash("Email does not exist.", category="error")
    return render_template("login_page.html", user=current_user)

@auth.route("/logout")
@login_required ##  Makes sure this route cannot be accessed unless the user is logged in
def logout_page():
    flash(f"{current_user.first_name} has Logged out!")
    logout_user()
    return redirect(url_for("auth.login_page"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up_page():
    """
        1.  Handles the sign up form and displaying of flash images
            and adding information to the database.
            Also handles redirecting after sign up.

        2. Ensures that Users that sign up do not already exist!
    """

    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password = request.form.get("password")
        password_confirm = request.form.get("passwordConfirm")

        ##  Prevents already-existing user from signing up
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists.", category="error") 
        elif len(email) < 4:
            ##  category='success' or category='error'
            flash("Email must be greater than 4 characters.", category='error')
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category='error')
        elif password != password_confirm:
            flash("Passwords do not match.", category='error')
        elif len(password) < 7:
            flash("Password must be at least 7 characters.", category='error')
        else:
            ##  Create a new user
            ##  'sha256_crypt' is a hashing method.
            ## For some reason, only 'pbkdf2:sha256' worked for me
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password, method='pbkdf2:sha256'))
            ##  add user to database
            DB.session.add(new_user)
            ##  Update the database
            DB.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            """ 
                To a new page
                'views.home' redirects to the url that maps to the function `home` belonging to the
                `views` blueprint
                This is done instead of url_for('/') because if the url route for the home function, "/",
                is ever changed, one will not need to update this code.
                so it is easier to just redirect to the funciton via it's blueprint, after which
                will determine the appropriate url """
            return redirect(url_for("views.home"))

    return render_template("sign-up_page.html", user=current_user)

