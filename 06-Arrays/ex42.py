def rand_elem(arr):
    import random
    y = len(arr)
    x = arr[random.randint(0,y-1)]
    return x
arrray = [1,2,3,4,5,6,7]
print(rand_elem(arrray))