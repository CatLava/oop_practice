# needed to nuke and pace

from contacts import AddressBook
from hr import PayrollSystem
from productivity import ProductivitySystem
from representations import AsDictionaryMixin



# Act as a database, not an actual database
# List of dictionarys,
class EmployeeDatabase:
    def __init__(self):
        # Example of composition
        self._employees = [
            {
            'id': 1,
            'name': 'John Doe',
            'role': 'manager'
            },

            {
                'id': 2,
                'name': 'Jane Doe',
                'role': 'secretary'
            },


            {
                'id': 3,
                'name': 'John Cena',
                'role': 'factory'
            },


            {
                'id': 4,
                'name': 'Bruce Willis',
                'role': 'sales'
            },


            {
                'id': 5,
                'name': 'Satoshi',
                'role': 'manager'
            }

        ]

        self.productivity = ProductivitySystem()
        self.employee_address = AddressBook()
        self.payroll = PayrollSystem()

    def employees(self):
        # This returns a new employee data set in one liner
        # Need to write this method for usage
        return[self._create_employee(**data) for data in self._employees]

    # _ means method should only be called in this class
    def _create_employee(self, id, name, role):
        address = self.employee_address.get_address(id)
        employee_role = self.productivity.get_role(role)
        employee_pay = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, employee_pay)




# Going to refactor this code
# using the dict ID mappings as a psuedo dastabase
class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        # Dict will filter out because of _ private indicator
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self.role.work(hours)
        print(f'{self.id} - {self.name}')
        print(f'- {duties}')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()



