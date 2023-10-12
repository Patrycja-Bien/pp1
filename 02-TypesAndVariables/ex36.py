buys = input("Enter buying rate: ")
sells = input("Enter selling rate: ")
buys = float(buys)
sells = float(sells)
spread = sells - buys
spread = "%.4f" % spread
print(f"Spread: {spread}")
