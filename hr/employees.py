# needed to nuke and pace

from contacts import get_address
from hr import get_policy, calculate_hours
from productivity import get_role, track
from representations import AsDictionaryMixin



# Act as a database, not an actual database
# List of dictionarys,
class _EmployeeDatabase:
    def __init__(self):
        # Example of composition
        self._employees = {
            1: {
            'name': 'John Doe',
            'role': 'manager'
            },

            2: {
                'name': 'Jane Doe',
                'role': 'secretary'
            },


            3: {
                'name': 'John Cena',
                'role': 'factory'
            },


            4: {
                'name': 'Bruce Willis',
                'role': 'sales'
            },


            5: {
                'name': 'Satoshi',
                'role': 'manager'
            }

        }

        self.productivity = ProductivitySystem()
        self.employee_address = AddressBook()
        self.payroll = PayrollSystem()

    def employees(self):
        # This returns a new employee data set in one liner
        # Need to write this method for usage
        #return[self._create_employee(**data) for data in self._employees]
        return [Employee(id_) for id_ in sorted(self._employees)]

    # _ means method should only be called in this class
    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError('invalid employee_id')
        return info




# Going to refactor this code
# using the dict ID mappings as a psuedo dastabase
class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = _EmployeeDatabase.get_employee_info(self.id)
        self.name = info.get('name')
        self._role = get_role(info.get('role'))
        self.address = get_address(self.id)
        self._payroll = get_policy(info.get(self.id))

    def work(self, hours):
        duties = self.role.work(hours)
        print(f'{self.id} - {self.name}')
        print(f'- {duties}')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()



