# This is where the hr.py will run
# We want to bring the classes into the namespace here

import hr

salary_employee = hr.SalaryEmployee(1, "John Smith", 1500)
hourly_employee = hr.HourlyEmployee(2, "John Doe", 40, 20)
commission_employee = hr.CommissionEmployee(3, " John Foo", 1000, 250)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])