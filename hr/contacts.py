# Creating an address class to model a street address
# We can't store it as string in case we want to pull info
# Between streets, states, cities, etc

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

address = Address("123 easy st.", "Omaha", "NE", 12305)
print(address)