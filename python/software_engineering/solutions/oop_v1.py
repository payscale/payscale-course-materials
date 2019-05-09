"""
Basic set of classes to represent a few animals.
This shows usage of instances and instance methods.
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
