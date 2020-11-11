N = int(input())

conference = [0] * N

for i in range(N):
    conference[i] = [int(x) for x in input().split()]

# conference 회의 시간 뒤에 끝나는 시간부터
conference.sort(key = lambda x : (x[1], x[0]))

# 결과에 반영될 변수
beforeEnd = conference.pop(0)[1]
count = 1

for start, end in conference:
    if(beforeEnd <= start):
        beforeEnd = end
        count += 1

print(count)