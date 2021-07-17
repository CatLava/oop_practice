# This will perform a function on this
class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('=======================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')

class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'

class SecretaryRole:
    # Will not use an init method
    def work(self, hours):
        print(f'does paper work for {hours} hours.')


class SalesRole:
    # Will not use an init method
    def work(self, hours):
        print(f'sells widgets for {hours} hours.')

class FactoryRole:
    # Will not use an init method
    def work(self, hours):
        print(f'constructs widgets for {hours} hours.')