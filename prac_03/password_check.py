"""a program that will make the user enter a password and display invalid if its not above a minimum length"""


def main():
    min_length = 6
    password = get_password(min_length)
    display_asterisk(password)


def display_asterisk(password):
    print(len(password) * "*", "was set!")


def get_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print("invalid")
        password = input("Enter password")
    return password


main()
