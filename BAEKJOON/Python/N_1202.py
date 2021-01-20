import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for i in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(jewels, (weight, value))
bags = [int(input()) for _ in range(K)]
bags.sort()

heap = []
result = 0
for i in range(K):
    while jewels and bags[i] >= jewels[0][0]:
        weight, value = heapq.heappop(jewels)
        heapq.heappush(heap, -1 * value)
    
    if heap:
        result -= heapq.heappop(heap)
    elif not jewels:
        break
    
print(result)