price_now = 90
price_then = 200
discount = 100 - (price_now*100)/price_then

if discount >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {discount}%")