import sys
input = sys.stdin.readline

N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]

# deadline 을 오름차순으로 sort
works.sort(key = lambda x : x[0])

import heapq

pq = []
for deadline, num in works:
  length = len(pq)
  # deadline 만큼 일 한다고 가정
  if length < deadline:
    heapq.heappush(pq, num)
  
  # 제일 작은 것은 바로 내동댕
  elif pq[0] < num:
    heapq.heappush(pq, num)
    heapq.heappop(pq)

result = 0
while pq:
  result += heapq.heappop(pq)

print(result)