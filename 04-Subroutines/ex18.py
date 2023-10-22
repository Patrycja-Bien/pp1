def numbers(n):
    display = ""
    display = list(display)
    for i in range(1, n+1):
        display.append(i)
    print(f"Numbers <1,{n}>:"," ".join(str(x) for x in display))

numbers(15)
numbers(7)