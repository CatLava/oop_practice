# This is where the hr.py will run
# We want to bring the classes into the namespace here

# This is v2 reformatting this entire file
#
# Policy based design
# Modules are in charge of various areas to perform a function

import json
from hr import calculate_hours, LTDPolicy
from productivity import track
from employees import employee_database, Employee

def print_dict(d):
    print(json.dumps(d, indent=2))

employees = employee_database.employees()

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_hours(employees)