class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # This is a built in function for only car
    # Put a repr on any defined class, this helps to understand it
    def __repr__(self):
        return 'Car({self.mileage})'.format(self=self)
    # Python built in method for string
    def __str__(self):
        return "a {self.color} car".format(self=self)

myc = Car("red", 12000)


myc
# when this is printed, all we get is a memory address, no information
print(myc)

# To help print readable information, we will use the __str__ and __repr__ methods

# __str__ is supposed to be easy to read function and be explicit as possible

