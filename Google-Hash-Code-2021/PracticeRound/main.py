a = "a_example"
b = "b_little_bit_of_everything.in"
c = "c_many_ingredients.in"
d = "d_many_pizzas.in"
e = "e_many_teams.in"

# 파일 읽어오기
def Read_File_Suck(path):
    import heapq

    with open("./source/" + path, 'r') as file:
        tempLine = list(map(int, file.readline().split()))
        pizzaCount = tempLine[0]
        Team = tempLine[1:]
        ingredient = []
    
        for n in range(pizzaCount):
            string = file.readline().split()
            heapq.heappush(ingredient, (-int(string[0]), string[1:], n))

    return (Team, pizzaCount, ingredient)

# 입력받기
Team, pizzaCount, ingredient = Read_File_Suck(d)

# 겹치는거 검사? ㅇㅇ got it
# 피자를 2개 -> 3개 -> 4개 순으로 검색
# 이 때 각 Process 에서 갯수가 늘어나지 않으면 전진하지 않고 그 Process 를 채택
finalResult = []
finalScore = []

for alpha, value in enumerate(ingredient):
    # 전부 선택했다면 Finish
    if (not Team[0]) and (not Team[1]) and (not Team[2]):
        break

    result = [value[2]]
    nowPizzas = set(value[1])
    nowLength = len(nowPizzas)

    ingredient.pop(alpha)

    betaBestIndex = -1
    for beta, nextValue in enumerate(ingredient):
        if nextValue[2] in result:
            continue

        tempLength = len(nowPizzas | set(nextValue[1]))
        if tempLength > nowLength:
            nowLength = tempLength
            betaBestIndex = beta

    if betaBestIndex == -1:
        betaCount, betaValue, betaIndex = ingredient.pop(-1)
        result.append(betaIndex)
        nowPizzas = nowPizzas | set(betaValue)
        nowLength = len(nowPizzas)
    else:
        betaCount, betaValue, betaIndex = ingredient.pop(betaBestIndex)
        result.append(betaIndex)
        nowPizzas = nowPizzas | set(betaValue)
        nowLength = len(nowPizzas)

    del betaBestIndex
    del betaCount
    del betaValue
    del betaIndex

    charlieBestIndex = -1
    for charlie, nextValue in enumerate(ingredient):
        if nextValue[2] in result:
            continue
        
        tempLength = len(nowPizzas | set(nextValue[1]))
        if tempLength > nowLength:
            nowLength = tempLength
            charlieBestIndex = charlie

    if (charlieBestIndex == -1 and (Team[0] != 0)) or (Team[0] != 0 and Team[1] == 0 and Team[2] == 0):
        Team[0] -= 1
        finalResult.append([2] + result)
        finalScore.append(nowLength)
        continue
    
    charlieCount, charlieValue, charlieIndex = ingredient.pop(charlieBestIndex)
    result.append(charlieIndex)
    nowPizzas = nowPizzas | set(charlieValue)
    nowLength = len(nowPizzas)

    del charlieBestIndex
    del charlieCount
    del charlieValue
    del charlieIndex

    deltaBestIndex = -1
    for delta, nextValue in enumerate(ingredient):
        if nextValue[2] in result:
            continue
        tempLength = len(nowPizzas | set(nextValue[1]))
        if tempLength > nowLength:
            nowLength = tempLength
            deltaBestIndex = delta

    if (deltaBestIndex == -1 and (Team[1] != 0)) or (Team[1] != 0 and Team[2] == 0):
        Team[1] -= 1
        finalResult.append([3] + result)
        finalScore.append(nowLength)
        continue
    
    deltaCount, deltaValue, deltaIndex = ingredient.pop(deltaBestIndex)
    result.append(deltaIndex)
    nowPizzas = nowPizzas | set(deltaValue)
    nowLength = len(nowPizzas)
    
    if Team[2] != 0:
        Team[2] -= 1
        finalResult.append([4] + result)
        finalScore.append(nowLength)

# 점수 계산하기
def Calc_Score(ingredient):
    ans = 0
    for i in range(len(ingredient)):
        ans += ingredient[i] * ingredient[i]
    # print("점수: \t", ans)

    return ans

print(Calc_Score(finalScore))

# 결과 저장
finalResult.sort()
finalLength = len(finalResult)

with open("./Submission.txt", 'w') as f:
    # 총 인원
    f.write(str(finalLength)+ "\n")

    for member in finalResult:

        # i팀 인원
        f.write(str(member[0])+ " ")

        for i in member[1:]:

            # 각 재료, 마지막에 공백이 포함된다 => 출력 형식 주의
            f.write(str(i)+" ")
        
        f.write("\n")