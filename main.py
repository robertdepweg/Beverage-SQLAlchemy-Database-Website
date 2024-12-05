"""Tiny Flask Example

From https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

Requires you to install flask in your virtual environment:

  $ . .venv/Scripts/activate

  $ python -m pip install flask

To run this on windows:

  Activate your environment if you haven't already.

  $ flask --app main run

Then in a browser go to http://127.0.0.1:5000/
"""

# Third-Party Imports
from flask import Flask

# First-Party Imports
from views.home import (
    home_view,
    contact_view
)
from views.employee import (
    employee_list_view,
    employee_add_view,
    employee_edit_view,
    employee_delete_view,
)

app = Flask(__name__)
# Define the secret key for use with cookies and the session
# (Don't leave this secret key within the code to GitHub in the future,
# you can use an env to get around this though.)
app.secret_key = b"lNJ9SacfBICdFwyqpwIODpMvX7r7pbJ-KnkM59A4nlA"

# @app.route() lets you set the url path that will trigger each view.
# '/' is the root of the domain. If your website was hosted at example.com
# then the full url would be https://example.com/
# If the path was '/do/thing/' then the full url would be https://example.com/do/thing/

# Define the routes for the app
app.add_url_rule("/", view_func=home_view)
app.add_url_rule("/contact", view_func=contact_view)
app.add_url_rule("/employees", view_func=employee_list_view)
app.add_url_rule("/employees/add", view_func=employee_add_view, methods=["GET", "POST"])
app.add_url_rule(
    "/employees/<int:pk>/edit",
    view_func=employee_edit_view,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/employees/<int:pk>/delete",
    view_func=employee_delete_view,
    methods=["GET", "POST"],
)
