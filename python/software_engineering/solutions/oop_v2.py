"""Use inheritance to factor out some common code."""


class Animal:

    def __init__(self, name):
        self.name = name


class Cow(Animal):

    def speak(self):
        print(f"Moo name is {self.name}")


class Cat(Animal):

    def speak(self):
        print(f"Meow name is {self.name}")


class Human(Animal):

    def speak(self):
        print(f"My name is {self.name}")


thomas = Human("Thomas")
thomas.speak()

betsy = Cow("Betsy")
betsy.speak()

lb = Cat("LB")
lb.speak()
