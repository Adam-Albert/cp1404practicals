"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount
is displayed on the screen.

"""
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("number of items cannot be less then 1")
    number_of_items = int(input("Number of items: "))
price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    while price_of_item <= 0:
        print("invalid price")
        price_of_item = float(input("Price of item: "))
    price += price_of_item
if price > 100:
    discount = price * 0.10
    print(f"Total price for {number_of_items} items is ${price - discount:.2f} ")
else:
    print(f"Total price for {number_of_items} items is ${price:.2f} ")
