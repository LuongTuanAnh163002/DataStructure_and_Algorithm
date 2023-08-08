def Quicksort(arr, l, r):
    p = arr[(l + r) // 2]
    i = l
    j = r
    while i < j:
        while arr[i] < p:
            i += 1
        
        while arr[j] > p:
            j -= 1
            
        if i <= j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1
    if i < r:
        Quicksort(arr, i, r)
    if l < j:
        Quicksort(arr, l, j)
        
arr = [12, 11, 13, 5, 6, 7]
n = len(arr) - 1
Quicksort(arr, 0, n)
print(arr)
