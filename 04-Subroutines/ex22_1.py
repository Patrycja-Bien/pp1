def month(n):
    if n == 1:
        return "January"
    elif n == 2:
        return "February"
    elif n == 3:
        return "March"
    elif n == 4:
        return "April"
    elif n == 5:
        return "May"
    elif n == 6:
        return "June"
    elif n == 7:
        return "July"
    elif n == 8:
        return "August"
    elif n == 9:
        return "September"
    elif n == 10:
        return "October"
    elif n == 11:
        return "November"
    else:
        return "December"
    
def month2(n):
    li = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return li[n-1]