import heapq

def heapsort(arr):
    heap = []
    heapq.heapify(heap)
    for i in arr:
        heapq.heappush(heap, i)
    for i in range(len(arr)):
        arr[i] = heapq.heappop(heap)
        
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print(arr)