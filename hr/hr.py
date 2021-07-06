class PayrollSystem:
    # Must be passed in as a list
    def calculate_payroll(self, employees):
        print("calculating payroll")
        print("===========")
        for employee in employees:
            print(f'Payroll for : {employee.id} + {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')


# This will be the parent class associated with this
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        # We want to initialize parent method
        # We can do this with super
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate




class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        # Inherits from the other
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission