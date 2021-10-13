"""
CP1404/CP5632 Practical
unreliable car test.
"""
from unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("car 1", 100, 79)
    car.drive(40)
    print(car)
    print(car.odometer)


main()
