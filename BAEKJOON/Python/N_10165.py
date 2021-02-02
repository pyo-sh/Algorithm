import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

bus = []

# (시작점, 끝점, 버스노선) 으로 저장
# 원형에서 0을 지나는 애들은 N 만큼 더해준다
# 0을 지나는 애들의 제일 큰 수를 beforeEnd 로 둔다 (제일 처음 비교 대상을 먹기 때문)
beforeEnd = 0
for index in range(1, M + 1):
    start, end = map(int, input().split())
    if start > end:
        beforeEnd = max(beforeEnd, end)
        end += N
    bus.append((start, end, index))

# 시작은 오름차순, 같다면 끝이 내림차순 으로 정렬
bus.sort(key = lambda x: (x[0], -x[1]))

result = []
beforeIndex = 0
# 뒤의 버스는 앞의 버스를 포함할 수 없다
for start, end, index in bus:
    if not end <= beforeEnd:
        beforeEnd = end
        result.append(beforeIndex)
        beforeIndex = index

result.append(beforeIndex)
result.sort()

string = ''
for index in result:
    if index != 0:
        string += str(index) + ' '

print(string[:-1])