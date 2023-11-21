def second_largest(arr):
    s = sorted(arr)
    return s[-2]
def diff(arr):
    big = max(arr)
    small = min(arr)
    return big - small
def median(arr):
    y = sorted(arr)
    x = len(y)
    if x%2 == 0:
        i = y[x//2 - 1]
        j = y[x//2]
        return (i + j )/2
    else:
        return y[x//2]
def sm_lg(arr):
    big = max(arr)
    small = min(arr)
    new = []
    new.append(small)
    new.append(big)
    return new
def string(arr):
    x = ""
    for i in arr:
        x += str(i) + "-"
    return x[:-1]
