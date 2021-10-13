"""
CP1404/CP5632 Practical
Taxi Test
"""

from taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(120)
    print(f"{taxi} \nCurrent fare: {taxi.get_fare()}")
    taxi.start_fare()
    print(f"{taxi} \nCurrent fare: {taxi.get_fare()}")


main()
