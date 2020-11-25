# python N_3163.py

from collections import deque

T = int(input())
answer = []

for i in range(T):
    N, L, k = map(int, input().split())

    # 개미들이 충돌하거나 안하거나 결국 떨어지는건 왼쪽, 오른쪽 순으로 떨어진다.
    # 개미가 충돌을 한 것과 안 한 것의 전체 시간은 같다 (순서가 달라질 뿐 떨어지는 시간은 같다)
    # 떨어지는 것을 구해서 정렬 -> 왼쪽, 오른쪽 차례차례로 떨어뜨린다.
    
    # 입력 받기
    ants = deque()
    justFall = [0] * N
    for n in range(N):
        antPosition, antID = list(map(int, input().split()))
        ants.append([antPosition, antID])
        
        # (충돌이 안 한다고 가정했을 때)
        # 왼쪽으로 향하는 개미는 position이 떨어지는 숫자이다.
        # 오른쪽으로 향하는 개미는 L - position이 떨어지는 숫자이다
        if antID > 0:
            antPosition = L - antPosition
        justFall[n] = [antPosition, antID]

    justFall.sort(key = lambda x: (x[0], x[1]))

    race = []
    count = 0
    while ants:
        # 떨어지는 시간이 같은 것을 찾아낸다.
        if count != N - 1 and justFall[count][0] == justFall[count + 1][0]:
            # 같이 떨어질 때 ID를 비교해서 순서를 찾는다.
            if ants[0][1] < ants[-1][1]:
                race.append(ants.popleft())
                race.append(ants.pop())
            else:
                race.append(ants.pop())
                race.append(ants.popleft())
            count += 2
        
        else:
            # 다음 떨어지는 녀석은 왼쪽 방향이다?
            # 그럼 왼쪽을 떨어뜨린다.
            if justFall[count][1] < 0:
                race.append(ants.popleft())
            # 다음 떨어지는 녀석이 오른쪽 방향이다?
            # 그럼 오른쪽을 떨어뜨린다.
            else:
                race.append(ants.pop())
            count += 1
        
    answer.append(race[k - 1][1])

for ans in answer:
    print(ans)