#   Fullstack Note Keeping Flask Web App


##	About App

### Requirements
Run `pip install flask flask-login flask-sqlalchemy`

###	Brief Description
   	A web application with secure user login authentication using a password and username and a
    database to store user details; it provides a simple Note taking service with a simple UI that allows
    users to write notes and store them securely on a server using webapps. 

###	Elaboration
    It involved the use of Flask and Flask-SQLAlchemy to produce the functionality of a cloud-oriented web app where
    every user has their own space and _data_categories/PROJECTS/PERSONAL on the app. The client's data is served from the
    server-side of the app, which is the same place where user authentication is done.
    Users can create as many accounts as they want and access the Note creating service.
    They can create notes, edit them, and delete them.
    The UI provides responses that make interaction livelier, such as pop-up messages to show when a user has logged in
    or logged out, or when a note has been added.
    Passwords and user information are stored securely using encryption on a database that contains hashed
    data so it cannot be read from the server-side. I use pbkdf2 hashing, which uses
    SHA-256 repeatedly, with salting, to make the hashing more secure.

    From this project I became even better versed with the Flask module; I implement the use of blueprints to separate
    different functionality into their own separate server-side Python scripts; the Blueprints can have their own
    endpoints, and even their own url prefix or domain begore accessing their endpoints.

    I also create the data base models to represent a User and a Note object. SQLAlchemy
    makes querying easier and more robust, effectively preventing SQL injections because of how it queries the
    database using Python.

###	Screenshots
![1](./scrn_shots/scrn_shot (1).png)
![2](./scrn_shots/scrn_shot (2).png)
![3](./scrn_shots/scrn_shot (3).png)
![4](./scrn_shots/scrn_shot (4).png)
![5](./scrn_shots/scrn_shot (5).png)

###	References
Tech With Tim (2021), "Python Website Full Tutorial - Flask, Aunthentication, Databases", [Youtube]
Finished: Sat-18-May-2024