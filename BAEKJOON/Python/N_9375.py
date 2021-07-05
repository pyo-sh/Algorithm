for _ in range(int(input())):
    clothes = [input().split() for _ in range(int(input()))]
    clothes.sort(key=lambda x: (x[1], x[0]))

    if len(clothes) == 0:
        print(0)
    else:
        before_cloth, before_type = clothes.pop(0)
        
        result = [1]
        for cloth, type in clothes:
            if type != before_type:
                result.append(1)
            elif cloth != before_cloth:
                result[-1] += 1
            before_cloth, before_type = cloth, type
        
        count = 1
        for num in result:
            count *= (num + 1)
        print(count - 1)