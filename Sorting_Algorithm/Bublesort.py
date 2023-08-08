def Bubblesort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    
a = [9, 5, 6, 1, 4, 7, 5]
Bubblesort(a)
print(a)




