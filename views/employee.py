"""Employee Views"""

# Third-Party Imports
from flask import flash, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# First-Party Imports
from models.employee import Employee

# Create database session
engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()


def employee_list_view():
    """Display a list of employess from the database"""
    employees = db_session.query(Employee).all()

    return render_template(
        # Template of context
        "employee/employee_list.html",
        # Variables it needs
        employees=employees,
    )

def employee_add_view():
    """Allow adding a new Employee to the database"""

    # Return the form for adding a new employee
    return render_template(
        "employee/employee_add.html",
    )