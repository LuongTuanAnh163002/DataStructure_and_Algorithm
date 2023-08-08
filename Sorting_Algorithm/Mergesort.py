def Merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    arr1 = [0] * n1
    arr2 = [0] * n2
    for i in range(n1):
        arr1[i] = arr[l + i]
    
    for j in range(n2):
        arr2[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = arr1[i]
        k += 1
        i += 1
    
    while j < n2:
        arr[k] = arr2[j]
        k += 1
        j += 1

def Mergsort(arr, l, r):
    if l < r:
        mid = l + (r - l)// 2
        Mergsort(arr, l, mid)
        Mergsort(arr, mid + 1, r)
        Merge(arr, l, mid, r)
    
    
arr = [9, 8, 8, 5, 5, 6, 7, 1, 2]
n = len(arr) - 1
Mergsort(arr, 0, n)
print(arr)
