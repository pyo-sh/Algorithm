import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [0] * N
for i in range(N - 1, -1, -1):
    coins[i] = int(input())

count = 0
for i in range(N):
    plusCoin = K // coins[i]
    count += plusCoin
    K -= coins[i] * plusCoin
    if K == 0:
        break
        
print(count)