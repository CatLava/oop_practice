class MyClass:
    def method(self):
        return 'instance method called', self

    #only has access to this parameter, only access the object representatiing the class
    # will not access the self method
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    # decorator, does not take any arguments at all,
    # name space the method
    @staticmethod
    def staticmethod():
        return 'static method called'


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def hawaiin(cls):
        return cls(['cheese', 'pineapple', 'ham'])

# when to use static method