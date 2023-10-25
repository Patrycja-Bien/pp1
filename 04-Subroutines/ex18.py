def numbers(n):
    display = ""
    display = list(display)
    for i in range(1, n+1):
        display.append(i)
    return " ".join(str(x) for x in display)

print(f"Numbers <1,15>: {numbers(15)}")
print(f"Numbers <1,7>: {numbers(7)}")