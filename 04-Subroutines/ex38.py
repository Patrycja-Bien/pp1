def f(palindrome):
    back = palindrome[::-1]
    if back == palindrome:
        return True
    else:
        return False
print(f("radar"))
print(f("12-11-21"))
print(f("book"))