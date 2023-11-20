def month(n):
    x = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return x[n-1]

y = int(input("Enter month number: "))
print(f"Month name: {month(y)}")
