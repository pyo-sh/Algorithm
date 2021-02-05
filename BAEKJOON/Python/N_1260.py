import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

history = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
  node1, node2 = map(int, input().split())
  history[node1][node2] = True
  history[node2][node1] = True

def printArray(result):
  string = ''
  for num in result:
    string += str(num) + ' '
  print(string[:-1])

# DFS  
stack = [V]
check = [False] * (N + 1)
result = []

while stack:
  node = stack.pop()
  if not check[node]:
    check[node] = True
    result.append(node)
    
    for i in range(N, 0, -1):
      if history[node][i] and not check[i]:
        stack.append(i)

printArray(result)

# BFS
queue = [V]
check = [False] * (N + 1)
result = []

while queue:
  node = queue.pop(0)
  if not check[node]:
    check[node] = True
    result.append(node)
    
    for i in range(1, N + 1):
      if history[node][i] and not check[i]:
        queue.append(i)

printArray(result)