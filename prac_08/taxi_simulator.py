"""
CP1404/CP5632 Practical
taxi simulator.
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "(Q)uit, (C)hoose, (D)rive"


def main():

    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    option = input(">>>").upper()
    total_bill = 0

    while option != "Q":

        if option == "C":
            print("taxis available")
            for i, taxi in enumerate(taxis, 1):
                print("{}, {}".format(i, taxi))
            choice = int(input("chose taxi: "))
            if choice > len(taxis) or choice < 1:
                print("invalid")
            else:
                current_taxi = taxis[choice - 1]

        elif option == "D":
            if current_taxi is None:
                print("you must choose a taxi first")
            else:
                current_taxi.start_fare()
                distance = int(input("drive how far?\n>>>"))
                current_taxi.drive(distance)
                fare_price = current_taxi.get_fare()
                total_bill += fare_price
                print("your trip cost you ${:.2f}".format(fare_price))

        else:
            print("invalid choice")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        option = input(">>>").upper()

    print("total bill is: ${:.2f} \nthank you for choosing this taxi service!".format(total_bill))


main()
