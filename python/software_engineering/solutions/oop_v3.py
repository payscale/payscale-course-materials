"""Use class variabls to factor out even more code."""


class Animal:
    POSSESIVE_ADJ = "My"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.POSSESIVE_ADJ} name is {self.name}")


class Cow(Animal):
    POSSESIVE_ADJ = "Moo"


class Cat(Animal):
    POSSESIVE_ADJ = "Meow"


class Human(Animal):
    pass


thomas = Human("Thomas")
thomas.speak()

betsy = Cow("Betsy")
betsy.speak()

lb = Cat("LB")
lb.speak()
