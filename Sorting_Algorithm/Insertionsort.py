def Insertionsort(arr):
    for i in range(1, len(arr)):
        indext = i
        value = arr[i]
        while indext > 0 and value < arr[indext - 1]:
            arr[indext] = arr[indext - 1]
            indext -= 1
        arr[indext] = value
    
arr = [8, 0, 9, 6, 1, 4, 5, 6]
Insertionsort(arr)
print(arr)