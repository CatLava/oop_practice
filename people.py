class Person:
    description = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("My name is {} and I'm {} years old".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}".format(self.name, food))

    def action(self):
        print("{} jumps".format(self.name))

class Baby(Person):
    description = "baby"

    def speak(self):
        print("bah bah")

    def nap(self):
        print("{} takes a nap".format(self.name))

nick = Person("Nick", 20)

nick.speak()

nick.eat("toast")

nick.action()

bab = Baby("Todd", 1)

bab.speak()

bab.eat("paste")

bab.action()

print(bab.description)
print(nick.description)