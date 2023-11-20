def f(binary_number):
    binary_number = str(binary_number)
    for i in binary_number:
        if i == "1" or i == "0":
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))