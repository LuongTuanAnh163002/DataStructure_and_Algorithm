def sortstack(arr):
    tmpstack = []
    while len(arr) > 0:
        tmp = arr[-1]
        arr.pop()
        while len(tmpstack) > 0 and tmpstack[-1] < tmp:
            arr.append(tmpstack[-1])
            tmpstack.pop()
            
        tmpstack.append(tmp)
    return tmpstack    

def sortarray(arr):
    new_stack = sortstack(arr)
    new_array = []
    while len(new_stack) > 0:
        new_array.append(new_stack[-1])
        new_stack.pop()
        
    return new_array

arr = [1, 9, 8, 6, 10, 4]
new_arr = sortarray(arr)
print(new_arr)