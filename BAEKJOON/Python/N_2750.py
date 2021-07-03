N = int(input())
array = [int(input()) for _ in range(N)]

def heapify(heap, index):
    child = 2 * index + 1
    # Choose child Left or Right
    if child < len(heap) - 1 and heap[child] > heap[child + 1]:
        child += 1
    # Check indexs
    if index < len(heap) and child < len(heap):
        # Max or Min
        if heap[index] > heap[child]:
            heap[index], heap[child] = heap[child], heap[index]
    # Childs Do
    if child <= len(heap) // 2: heapify(array, child)

# Heapify Half to Top
for i in reversed(range(len(array)//2)):
    heapify(array, i)

# Sorted
for i in reversed(range(len(array))):
    array[0], array[i] = array[i], array[0]
    print(array.pop())
    heapify(array, 0)