# Base class for vehicles
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving at {self.speed} km/h 🚗"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying at {self.speed} km/h ✈️"


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing at {self.speed} knots ⛵"


# Base class for animals
class Animal:
    def __init__(self, species, speed):
        self.species = species
        self.speed = speed
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Cheetah(Animal):
    def move(self):
        return f"The {self.species} sprints across the savannah at {self.speed} km/h 🐆"


class Eagle(Animal):
    def move(self):
        return f"The {self.species} soars through the sky at {self.speed} km/h 🦅"


class Turtle(Animal):
    def move(self):
        return f"The {self.species} crawls slowly at {self.speed} km/h 🐢"


# Polymorphic behavior demonstration
things_that_move = [
    Car("Tesla Model S", 120),
    Plane("Boeing 747", 900),
    Boat("Sailor One", 40),
    Cheetah("Cheetah", 120),
    Eagle("Eagle", 160),
    Turtle("Turtle", 1)
]

# Each object responds to move() differently
for thing in things_that_move:
    print(thing.move())
