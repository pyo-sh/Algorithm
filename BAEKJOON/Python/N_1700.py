import sys
input = sys.stdin.readline

N, K = map(int, input().split())
schedule = list(map(int, input().split()))

plug_set = set()

countUse = 0
lastPlug = -1
result = 0

for i in range(K):
  nowPlug = schedule[i]
  # 플러그가 도킹되어 있지 않을 때만을 고려
  if not nowPlug in plug_set:
    # 플러그를 꼽아야 하지만 자리가 남는다면
    if countUse < N:
      countUse += 1
    
    # 플러그를 꼽아야 하지만 자리가 없네?
    else:
      future_plug = set(plug_set)
      # 뒤의 스케쥴을 검사한다
      for num in schedule[i + 1:]:
        # 플러그에 하나만 남는다면 그것이 뽑을 것
        if len(future_plug) < 2:
          break
        
        # 플러그에 꼽혀 있는 것이 있다면 미리 뽑아본다
        if num in future_plug:
          future_plug.discard(num)
      
      # 교체 한다
      plug_set.discard(future_plug.pop())
      result += 1
      
    # 현재 플러그를 꼽는다
    plug_set.add(nowPlug)
    lastPlug = nowPlug
    
print(result)
