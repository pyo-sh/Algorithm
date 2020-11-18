N = int(input())

wire = int(input())
history = {}
for i in range(wire):
    a, b = map(int, input().split())
    if a in history:
        history[a].append(b)
    else:
        history[a] = [b]
    if b in history:
        history[b].append(a)
    else:
        history[b] = [a]

from collections import deque

infected = set()
infected.add(1)
queue = deque()
queue.append(1)

result = -1

while queue:
    virus = queue.popleft()

    if virus in history:
        for infection in history[virus]:
            if not infection in infected:
                queue.append(infection)
                infected.add(infection)
    
    result += 1

print(result)