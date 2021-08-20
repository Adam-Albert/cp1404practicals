out_file = open("name.txt", "w")
name = input("name>>>")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt")
name = in_file.read()
in_file.close()
print("your name is {}".format(name))

in_file = open("numbers.txt", "r")
numbers = in_file.read().strip()
first_number = int(numbers[:3])
second_number = int(numbers[2:5])
in_file.close()
sum_of_num = first_number + second_number
print(sum_of_num)

in_file = open("numbers.txt", "r")
sum_of_num = 0
for line in in_file:
    number = int(line)
    sum_of_num += number
in_file.close()
print(sum_of_num)
