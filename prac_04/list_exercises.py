""" 1. Basic list operations"""

numbers = []
for i in range(0, 5):
    number = int(input("number>>"))
    numbers.append(number)
print("the first number is {}\nthe last number is {}\n"
      "the smallest number is {}\nthe largest number is {}\nthe average of the numbers is {}"
      .format(numbers[0], numbers[-1], min(numbers), max(numbers), (sum(numbers) / len(numbers))))


""" 2 Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("username>>>")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
