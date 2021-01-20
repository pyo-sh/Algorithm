import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))

dp_up = [0] * N
dp_down = [0] * N

result = 0
for x in range(N):
    dp_up[x] = 1
    x_reverse = N - x - 1
    dp_down[x_reverse] = 1
    for y in range(x):
        # 가장 긴 증가하는 부분 수열 구하기
        if array[y] < array[x] and dp_up[y] + 1 > dp_up[x]:
            dp_up[x] = dp_up[y] + 1
        # 가장 긴 감소하는 부분 수열 구하기 (반대로 진행해야 한다..)
        y_reverse = N - y - 1
        if array[y_reverse] < array[x_reverse] and dp_down[y_reverse] + 1 > dp_down[x_reverse]:
            dp_down[x_reverse] = dp_down[y_reverse] + 1

for i in range(N):
    result = max(result, dp_up[i] + dp_down[i])

# 결과 값에 마지막을 하는 이유?
# 왼쪽과 오른쪽에서 점점 증가하는 부분 수열을 구했을 때 마지막 값은 중복이기 때문이다
print(result - 1)