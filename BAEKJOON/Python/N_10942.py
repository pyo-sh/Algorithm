import sys
input = sys.stdin.readline
N = int(input())
board = list(map(int, input().split()))
M = int(input())
dp = [[False for _ in range(N + 1)] for __ in range(N + 1)]

dp[0][0] = True
for i in range(1, N + 1):
    # 길이 0, 1 은 펠린드롬이다
    dp[i][i] = True 
    dp[i][i-1] = True

# 전체 배열에 대해서 2 차원 배열로 회문인지 전부 계산한다.
# S, E를 받고 나서 검사하는 것보다 전부 검사하고 난 뒤 dp를 이용하는 것이 더 이득이다
# 길이가 1 ~ N 인 회문을
for length in range(1, N + 1):
    # 1번부터 N 까지 전부 검사한다
    for start in range(1, N - length + 1):
        # start번 의 숫자에서 length 이후까지
        end = start + length
        # 끝과 끝이 같고 양 쪽을 제외한 내부 배열이 Palindrome이면 결국 Palindrome이다
        dp[start][end] = dp[start + 1][end - 1] and board[start - 1] == board[end - 1]

for i in range(M):
    S, E = map(int, input().split())
    print(1 if dp[S][E] else 0)