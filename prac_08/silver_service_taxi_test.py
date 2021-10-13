"""
CP1404/CP5632 Practical
silver service test.
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("fancy taxi", 100, 2.10)
    taxi.drive(20)
    print(taxi)
    print(taxi.get_fare())


main()
