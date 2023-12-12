def f(arr):
    check = []
    for i in arr:
        if arr.count(i) > 1:
            continue
        else:
            check.append(i)
    return int(check[0])

if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))