# prints 1 to 20 in steps on 2
for i in range(1, 21, 2):
    print(i, end=' ')

# prints 0 to 100 in steps of 10
for i in range(0, 101, 10):
    print(i, end=' ')

# prints 20 to 1 in steps of 1
for i in range(20, 0, -1):
    print(i, end=' ')

# prints stars depending on user input
number_of_stars = int(input("Number of Stars>>> "))
for i in range(number_of_stars):
    print("*", end=' ')
