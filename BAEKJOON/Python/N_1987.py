import sys
input = sys.stdin.readline

# A = 65, Z = 90
R, C = map(int, input().split())
alpha = [input() for _ in range(R)]

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

maximum = 0
def dfs(check, x, y, count):
    global R, C, alpha, direction, maximum

    check[ord(alpha[y][x]) - 65] = True
    maximum = max(maximum, count)

    for gx, gy in direction:
        dx, dy = gx + x, gy + y
        if 0 <= dx < C and 0 <= dy < R:
            if not check[ord(alpha[dy][dx]) - 65]:
                dfs(check[:], dx, dy, count + 1)

dfs([False] * 26, 0, 0, 1)
print(maximum)