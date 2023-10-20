N = int(input("Enter number: "))
prime = ""
prime = list(prime)

for i in range(2, N+1):
    if i > 1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
            prime.append(i)

print("Prime numbers:",' '.join(str(items) for items in prime))