"""
    Every html file is written in the `templates` folder.
    These are the html templates.
    In flask, when html is rendered, it's rendered as a template.
    This is because flask uses a unique templating language called `Jinga`
    This templating language enables one to write a bit of Python inside HTML documents.
    This replaces the need for javascript.
"""

from website import create_app  ##  Website has become a Python package because of __init__.py



app = create_app()



if __name__=="__main__":
    # with app.app_context():
    app.run(debug=True, port="4242")