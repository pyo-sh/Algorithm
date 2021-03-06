import sys
input = sys.stdin.readline

N, r, c= map(int, input().split())

# 내가 생각하는 x는 column, y는 row 임에 주의하자
direction = [(0, 0), (1, 0), (0, 1), (1, 1)]

result = 0

def check_RC(x, y, alpha):
    global result
    if x == c and y == r:
        print(result)
        return

    if x <= c < x + alpha and y <= r < y + alpha:
        beta = alpha // 2
        for dx, dy in direction:
            check_RC(x + dx * beta, y + dy * beta, beta)
        
    else:
        result += alpha * alpha

check_RC(0, 0, 2 ** N)