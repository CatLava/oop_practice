# Creating an address class to model a street address
# We can't store it as string in case we want to pull info
# Between streets, states, cities, etc

# will also create an address mapping class
# Map ids to address

class AddressBook:
    def __init__(self):
        self._employee_address = {
            1: Address('23 Maple St', 'Kansas City', 'Missouri', '87604'),
            2: Address('54 Sycamore Lane', 'Huntsville', 'Alabama', '56901'),
            3: Address('24 Sunny St', 'Baltimore', 'Maryland', '777453'),
            4: Address('99 Asher Road', 'Miami', 'Florida', '97855'),
            5: Address('574 Beach blvd', 'Anaheim', 'California', '97680')
        }

    def get_address(self, employee_id):
        address = self._employee_address.get(employee_id)
        if not address:
            raise ValueError('Invalid Address id')
        return address

class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # use magic method to get a string representation of the current object
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

