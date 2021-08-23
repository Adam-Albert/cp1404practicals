"""a program to calculate the monthly cumulative totals for incomes.
The program should ask for the number of monthly incomes to enter, then get and store the incomes in a list."""


def main():
    number_of_months = int(input("How many months? "))
    incomes = []
    for month in range(number_of_months):
        income = float(input("Enter income for month {}: ".format(month + 1)))
        incomes.append(income)
    print_report(number_of_months, incomes)


def print_report(number_of_months, incomes):
    total_income = 0
    print("\nIncome report\n-------------------")
    for month in range(number_of_months):
        total_income += incomes[month]
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, incomes[month], total_income))


main()
