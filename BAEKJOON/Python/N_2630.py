import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

direction = [(0, 0), (1, 0), (0, 1), (1, 1)]

def count_paper(x, y, alpha):
    countBlue = return_white = return_blue = 0
    for row in paper[y : y + alpha]:
        countBlue += row[x : x + alpha].count(1)

    if not countBlue:
        return_white = 1
    elif countBlue == alpha * alpha:
        return_blue = 1
    else:
        beta = alpha // 2
        for dx, dy in direction:
            temp_white, temp_blue = count_paper(x + dx * beta, y + dy * beta, beta)
            return_white += temp_white
            return_blue += temp_blue
    
    return (return_white, return_blue)

white, blue = count_paper(0, 0, N)
print(white)
print(blue)