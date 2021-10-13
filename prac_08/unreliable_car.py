"""
CP1404/CP5632 Practical
unreliable car class.
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """A variation of car"""

    def __init__(self, name, fuel, reliability):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if reliable."""
        will_drive = randint(0, 100) < self.reliability
        if will_drive:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0


