def main():
    try:
        numerator = get_valid_number("Enter the numerator: ")
        denominator = get_valid_number("Enter the denominator: ")
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

# When will a ValueError occur? // when a string is placed in the input

# When will a ZeroDivisionError occur? //  when both the numerator and denominator are zero

# Could you change the code to avoid the possibility of a ZeroDivisionError? // to not allow a zero to be added


def get_valid_number(prompt):
    number = int(input(prompt))
    while number == 0:
        print("invalid")
        number = int(input(prompt))
    return number


main()
