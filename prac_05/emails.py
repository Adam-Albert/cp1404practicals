
def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("is your name {} (Y/n)".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    name = email.split("@")[0]
    name_parts = name.split(".")
    full_name = " ".join(name_parts)
    return full_name


main()
