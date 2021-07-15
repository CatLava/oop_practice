# This is where the hr.py will run
# We want to bring the classes into the namespace here

import hr
import employees
import productivity

# Using further inherited classes here for representation
# This is part of the class explosion problem
manager = employees.Manager(1, "John Smith", 1500)
secretary = employees.Secretary(2, "John Doe", 500)
sales_guy = employees.SalesPerson(3, " John Foo", 1000, 250)
factory_worker = employees.FactoryWorker(4, "Pete Foo", 40, 25)
# This is double inheritance class
temp_secratary = employees.TemporarySecretary(5, "Susan", 40, 20)


employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temp_secratary
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)