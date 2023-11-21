arr1 = [1,2,3]
arr2 = [1,2,3,4,5]
def check(a1,a2):
    for i in a1:
        if i in a2:
            continue
        else:
            return False
    return True

print(check(arr1,arr2))
print(check(arr2,arr1))
        