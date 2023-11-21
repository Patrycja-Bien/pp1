def bubbleSort(arr):
    n = len(arr)
     
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

x = [9,8,7,6,5,4,3,2,1]
y = [12,6,6,23,67,1,2]
z = [1,2,0,0,1,2]

bubbleSort(x)
bubbleSort(y)
bubbleSort(z)

for i in range(len(x)):
        print(x[i], end=" ")
print()
for i in range(len(y)):
        print(y[i], end=" ")
print()
for i in range(len(z)):
        print(z[i], end=" ")
