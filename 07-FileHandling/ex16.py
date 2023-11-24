x = input("Enter file name: ")
count = 0
with open(x, 'r') as file:
    for line in file:
        count += 1
print(f"Number of lines: {count}")
