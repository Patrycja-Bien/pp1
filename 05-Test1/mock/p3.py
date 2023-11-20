def f(name):
    result = ""
    name = name.split(" ")
    for i in name:
        y = i[0]
        result += y
    return result


if __name__ == "__main__":
    print(f("Internet of Things")) #returns "IoT"
    print(f("For Your Information")) #returns "FYI"
    print(f("Python")) #returns "P"
