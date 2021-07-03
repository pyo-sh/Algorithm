def solution(n, computers):
    answer = 0
    
    check = [False] * n
    for i in range(len(computers)):
        if not check[i]:
            answer += 1
        
            stack = [i]
            while stack:
                node = stack.pop()
                
                if check[node]:
                    continue
                
                check[node] = True
                for x in range(len(computers)):
                    if computers[node][x] == 1 and not check[x]:
                        stack.append(x)
    
    return answer