"""a program that keeps a list of user guitars and then displayes them once the user enters an empty string"""

from guitar import Guitar


def main():
    """get guitars and add them to a list until nothing is entered then display all guitars """
    guitars = []
    print("My Guitars!")
    name, year, cost = get_input()
    guitar = Guitar(name, cost, year)
    while guitar.name != "":
        print("{} added!".format(guitar))
        guitars.append(guitar)
        name, year, cost = get_input()
        guitar = Guitar(name, cost, year)
    print("\n_______Snip________\n")
    display_guitars(guitars)


def display_guitars(guitars):
    """display all guitars"""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))
    else:
        print("no Guitars")


def get_input():
    """get all inputs for guitar class"""
    name = input("name: ")
    if name == "":
        return "", 0, 0
    year = get_valid_int("year: ")
    cost = get_valid_float("cost: ")
    return name, year, cost


def get_valid_float(prompt):
    """Get a valid float."""
    is_valid_input = False
    number = 0
    while not is_valid_input:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("invalid input; Enter a valid number")
    return number


def get_valid_int(prompt):
    """Get a valid int."""
    is_valid_input = False
    number = 0
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("invalid input; Enter a valid number")
    return number


main()
