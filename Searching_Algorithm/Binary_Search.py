def binary_search(arr, x, l, r):
    if l > r:
        return False
    else:
        mid = (l + r) // 2
        if x == arr[mid]:
            return True
        elif x < arr[mid]:
            return binary_search(arr, x, l, mid - 1)
        elif x > arr[mid]:
            return binary_search(arr, x, mid + 1, r)
arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 10, 0, 4))