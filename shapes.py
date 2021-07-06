
class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return self.length*2 + self.width*2

    def what_ami(self):
        return "Rectangle"

# Now if we want a square, it is still a Rectangle
# We want to implement inheritance on this class

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length, length)

    def what_ami(self):
        return "Square"


# cube will inherit from square
class Cube(Square):
    # no ned to redefine init because defined in square
    def surface_area(self):
        face_area = self.area()
        return face_area*6

    def volume(self):
        face_area = self.area()
        return face_area*self.length

    def what_ami(self):
        return "Cube"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_ami(self):
        return "Triangle"

# Now we will do multiple inheritance
# call the __mro__ on this for the method resolution order
# Depending on order of methods, it will call other areas
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['length'] = base
        super().__init__(base=base, **kwargs)

    def what_ami(self):
        return "Pyramid"

# Order of inheritance is critical
# Mixin is a class that is pulled in that won't have nay clashes.



