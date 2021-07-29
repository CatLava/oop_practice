# This will perform a function on this
# Make this class a singleton, only instantiated once
# This class is internal to the module
class _ProductivitySystem:
    def __init__(self):
        # Underscore is meant to keep it hidden
        # A method inside of this class will use it
        # More control over how data is accessed
        self._roles = {
            'manager' : ManagerRole,
            'secretary' : SecretaryRole,
            'sales' : SalesRole,
            'factory' : FactoryRole
        }

    def get_role(self, role_id):
        # Dictionary method to obtain the role ID
        role_type = self._roles.get(role_id)

        if not role_type:
            raise ValueError("invalid role_id")
        # This will instantiate it into an object
        return role_type()

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

_productivity_system = _ProductivitySystem()

def get_role(role_id):
    return _productivity_system.get_role(role_id)

def track(employees, hours):
    _productivity_system.track(employees, hours)