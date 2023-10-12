price = input("Enter price: ")
discount = input("Enter discount %: ")
price = float(price)
discount = float(discount)
discount = 100 - discount
price_w_discount = (price * discount) / 100
reduction = price - price_w_discount
price_w_discount = round(price_w_discount, 2)
reduction = round(reduction, 2)
print(f"Price with discount: {price_w_discount}")
print(f"Reduction: {reduction}")