sum = 0
nums = []
try:
    with open("numbers.txt", 'r') as file:
        for line in file:
            sum += int(line)
            nums.append(int(line))
        print(f"Numbers: {" ".join(str(i) for i in nums)}")
        print(f"Sum: {sum}")
except FileNotFoundError:
    print(f"File '{"numbers.txt"}' not found.")
