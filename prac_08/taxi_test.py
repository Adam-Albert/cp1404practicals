
from taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(f"{taxi} \nCurrent fare: {taxi.get_fare()}")
    taxi.start_fare()
    taxi.drive(100)
    print(f"{taxi} \nCurrent fare: {taxi.get_fare()}")


main()
