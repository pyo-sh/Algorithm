import sys
input = sys.stdin.readline

N = int(input())
board = [0] * N
result = 0

def n_Queen(index):
    global N, result, board
    if index >= N:
        result += 1
        return

    check = [True] * N
    for i in range(index):
        check[board[i]] = False
        diff = index - i
        if 0 <= board[i] + diff < N:
            check[board[i] + diff] = False
        if 0 <= board[i] - diff < N:
            check[board[i] - diff] = False
    
    for point in range(N):
        if check[point]:
            board[index] = point
            n_Queen(index + 1)

n_Queen(0)
print(result)