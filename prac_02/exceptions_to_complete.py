finished = False
result = 0
while not finished:
    try:
        number_01 = int(input("number_1>>>"))
        number_02 = int(input("number_2>>>"))
        result = number_01 + number_02
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
