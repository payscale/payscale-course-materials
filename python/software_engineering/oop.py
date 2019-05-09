"""
Here we will learn about basic object-oriented programming primatives.
We will study the python `class`, instance variables, class variables,
and inheritance.
"""


class Cow:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Moo name is {self.name}")


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Meow name is {self.name}")


class Human:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")


thomas = Human("Thomas")
thomas.speak()

betsy = Cow("Betsy")
betsy.speak()

lb = Cat("LB")
lb.speak()
