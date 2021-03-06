import sys
input = sys.stdin.readline

N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

# 행렬을 곱해서 반환해주는 함수
def get_multipled_matrix(matrix_A, matrix_B):
    global N
    temp_matrix = [[0] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            for c in range(N):
                temp_matrix[a][b] += matrix_A[a][c] * matrix_B[c][b]
            temp_matrix[a][b] %= 1000
    
    return temp_matrix

# 2진수로 바꾸어서 '1' 이면 제곱 후 A 곱해주기 '0' 이면 제곱 만 하기
# 맨 처음의 1 : ((A ** 0) ** 2) * A 이므로 제외하고 now_matrix 를 A로 준다.
bit_B = bin(B)[3:]
now_matrix = A
for char in bit_B:
    now_matrix = get_multipled_matrix(now_matrix, now_matrix)

    if char == '1':
        now_matrix = get_multipled_matrix(now_matrix, A)

# 마지막에도 1000을 나누지 않으면 오류가 나더라..
# 반 례
# 2 1
# 1000 1000
# 1000 1000
for arr in now_matrix:
    print(' '.join(map(lambda x: str(x % 1000), arr)))