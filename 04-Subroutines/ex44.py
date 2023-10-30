def f(password):
    check = ""
    for i in password:
        if i not in check:
            check += i
        else:
            continue
    if len(check) >= 6:
        return True
    else:
        return False

print(f("ax15")) 
print(f("book123"))
print(f("A2water3")) 
print(f("qwerty"))
print(f(""))
