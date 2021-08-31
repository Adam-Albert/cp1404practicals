"""A program that asks the user how many "quick picks" they wish to generate.
 The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45."""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("how many quick picks ? "))
for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_picks:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_picks.append(number)
        quick_picks.sort()
    print(" ".join("{:2}".format(number) for number in quick_picks))
