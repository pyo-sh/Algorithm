import sys
input = sys.stdin.readline

from collections import deque

def get_deepest(start):
    global tree
    visited = [False] * (n + 1)

    que = deque([(start, 0)])

    maxNode, maxDif = start, 0
    while que:
        node, dif = que.popleft()

        if visited[node]:
            continue

        visited[node] = True
        if maxDif < dif:
            maxNode, maxDif = node, dif

        for child, depth in tree[node]:
            if not visited[child]:
                que.append((child, dif + depth))

    return (maxNode, maxDif)

n = int(input())

if n == 1:
    print(0)
else:
    tree = [[] for _ in range(n + 1)]

    while True:
        a, b, depth = map(int, input().split())
        tree[a].append((b, depth))
        tree[b].append((a, depth))

        if b == n:
            break

    print(get_deepest(get_deepest(1)[0])[1])
