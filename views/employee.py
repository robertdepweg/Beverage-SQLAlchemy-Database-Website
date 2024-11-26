"""Employee Views"""

# Third-Party Imports
from flask import flash, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# First-Party Imports
from models.employee import Employee, Base

# Create database session
engine = create_engine("sqlite:///db.sqlite3", echo=False)
Base.metadata.create_all(engine)
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