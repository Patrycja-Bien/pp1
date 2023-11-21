def occurs(number, array):
    for i in array:
        if number == i:
            return True
        else:
            continue
    return False

num = int(input("Enter number: "))
arr = [15, 38, 7, 23, 14]

print(f"Number: {num}")
print(f"Array: {" ".join(str(i) for i in arr)}")
if occurs(num, arr) == True:
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} does NOT appear in the array")