def Selectionsort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        if mini != i:
            temp = arr[i]
            arr[i] = arr[mini]
            arr[mini] = temp
    
arr = [9, 8, 8, 5, 5, 6, 7, 1, 2]
Selectionsort(arr)
print(arr)

