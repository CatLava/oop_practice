# needed to nuke and pace

from contacts import AddressBook
from hr import PayrollSystem
from productivity import ProductivitySystem



# Act as a database, not an actual database
# List of dictionarys,
class EmployeeDatabase:
    def __init__(self):
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
            }


            {
                'id': 3,
                'name': 'John Cena',
                'role': 'factory'
            }


            {
                'id': 4,
                'name': 'Bruce Willis',
                'role': 'sales'
            }


            {
                'id': 5,
                'name': 'Satoshi',
                'role': 'manager'
            }

        ]

        self.productivity = ProductivitySystem()
        self.address = AddressBook()
        self.payroll = PayrollSystem()

    def employees(self):
        # This returns a new employee data set in one liner
        # Need to write this method for usage
        return[self._create_employee(**data) for data in self._employees]

    # _ means method should only be called in this class
    def _create_employee(self, id, name, role):




# Going to refactor this code
# using the dict ID mappings as a psuedo dastabase
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None


