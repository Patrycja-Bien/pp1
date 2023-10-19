pln = int(input("Enter the amount in PLN: "))
three = pln//5
two = pln%5
two = two//2
one = two%2
print(f"The amount of PLN in coins:")
print(f"5 zł - {three}")
print(f"2 zł - {two}")      
print(f"1 zł - {one}")
