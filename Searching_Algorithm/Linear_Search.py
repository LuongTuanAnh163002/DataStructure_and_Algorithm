def Linear_search(a, x):
    for i in a:
        if x == i:
            return 1
    return -1

a = [1, 2, 3, 4, 5, 6]
print(Linear_search(a, 2))
