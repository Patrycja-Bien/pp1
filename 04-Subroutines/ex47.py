def f(text):
    result = ""
    if len(text) <= 1:
        return text
    else:
        for i in text:
            if i == text[-1]:
                result += i
            else:
                result += i + "-"
    return result

print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))