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

    # List to store any errors encountered
    errors = []

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        weekly_salary = request.form["weekly_salary"]
        
        if not first_name:
            errors.append("The first name is required.")
        if not last_name:
            errors.append("The last name is required.")
        if not weekly_salary:
            errors.append("The weekly salary is required.")
        try:
            weekly_salary = float(weekly_salary)
        except Exception:
            errors.append("The weekly salary needs a proper dollar amount.")

        if not errors:
            # Create the new Employee
            new_employee = Employee(first_name, last_name, weekly_salary)
            db_session.add(new_employee)
            db_session.commit()

            flash("User added successfully!", "success")

            return redirect(url_for("employee_list_view"))
        
def employee_edit_view(pk):
    """Allow editing an existing Employee in the database"""

    # List to store any errors encountered
    errors = []

    employee = db_session.get(Employee, pk)

    if not employee:
        flash(f"Unknown employee with pk of {pk}", "danger")
        return redirect(url_for("employee_list_view"))

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        weekly_salary = request.form["weekly_salary"]
        
        if not first_name:
            errors.append("The first name is required.")
        if not last_name:
            errors.append("The last name is required.")
        if not weekly_salary:
            errors.append("The weekly salary is required.")
        try:
            weekly_salary = float(weekly_salary)
        except Exception:
            errors.append("The weekly salary needs a proper dollar amount.")

        if not errors:
            # Edit the new Employee
            employee.first_name = first_name
            employee.last_name = last_name
            employee.weekly_salary = weekly_salary
            db_session.commit()

            flash("User updated successfully!", "success")

            return redirect(url_for("employee_list_view"))

    # Return the form for adding a new employee
    return render_template(
        "employee/employee_edit.html",
        employee=employee,
        errors=errors,
    )
