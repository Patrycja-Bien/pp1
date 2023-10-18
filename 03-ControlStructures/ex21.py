first = input("Enter first number: ")
second = input("Enter second number: ")
first = int(first)
second = int(second)

if first > second:
    print(f"Numbers in ascending order: {second}, {first}")
else:
    print(f"Numbers in ascending order: {first}, {second}")