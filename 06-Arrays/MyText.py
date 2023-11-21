def numofwords(txt):
    for i in txt:
        x = txt.split(" ")
        return len(x)
def order(txt):
    x = txt.split(" ")
    return sorted(x, key=len, reverse=True)
def alph(txt):
    x = txt.split(" ")
    return sorted(x)