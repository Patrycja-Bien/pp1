def read_number():
    n1 = input("Enter a number: ")
    n2 = input("Enter a number: ")
    n1 = int(n1)
    n2 = int(n2)
    print(f"{n1} + {n2} = {n1 + n2}")


if __name__ == "__main__":
    read_number()