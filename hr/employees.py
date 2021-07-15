# This will be the parent class associated with this
# Also an abstract class, this is not meant to be called
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

'''
The below methods are used to make productivity measurements
This is also and example of the class explosion principle 
'''
class Manager(SalaryEmployee):
    # Will not use an init method
    def work(self, hours):
        print(f'{self.name} yells for {hours} hours.')

class Secretary(SalaryEmployee):
    # Will not use an init method
    def work(self, hours):
        print(f'{self.name} does paper work for {hours} hours.')


class SalesPerson(CommissionEmployee):
    # Will not use an init method
    def work(self, hours):
        print(f'{self.name} sells widgets for {hours} hours.')

class FactoryWorker(HourlyEmployee):
    # Will not use an init method
    def work(self, hours):
        print(f'{self.name} constructs widgets for {hours} hours.')

class TemporarySecretary(Secretary, HourlyEmployee):
    # multiple inheritance example, receive from other classes
    # being able to add this to certain scenarios
    # Think method resolution in order when working with Python
    # Below will bypass the MRO
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)