"""Home and static views"""

# Third-Party Imports
from flask import render_template


def home_view():
    """Home View"""
    return render_template("home.html")


def contact_view():
    """Contact View"""
    return render_template("contact.html")