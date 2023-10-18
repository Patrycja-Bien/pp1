items = input("Enter number of products: ")
price = input("Enter price: ")
items = int(items)
price = float(price)
if items >= 2:
    price_now = 0.75*price
    print(f"Numbers of products purchased: {items}")
    print(f"Product price: {price}")
    print(f"Amount to pay: {price_now}")
else:
    print(f"Numbers of products purchased: {items}")
    print(f"Product price: {price}")
    print(f"Amount to pay: {price}")