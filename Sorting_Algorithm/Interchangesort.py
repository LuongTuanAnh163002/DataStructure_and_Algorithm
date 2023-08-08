#Là sự kết hợp của bubblesort và selectionsort
def Interchangesort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    
arr = [12, 11, 13, 5, 6, 7]
Interchangesort(arr)
print(arr)