'''
Runtime : 28 ms(77.16%)
Memory : 13.8 MB(55.80%)
Combination을 사용하는 방법도 보아야 할 듯.
삼각형을 반으로 접어서 계산하여 메모리 용량을 줄어보려고 했다.
근데 그냥 푸는게 더 효율적인 것 같은 느낌이 든다.
'''
import math
class Solution:
    def getRow(self, rowIndex):
        # rowIndex 층에서 배열의 갯수는 rowIndex + 1 개 이므로
        n = rowIndex + 1
        
        # rowIndex 가 0 or 1 일 경우 아래 알고리즘을 수행할 수 없어 지정한 답을 내놓게 함
        if rowIndex < 2:
            return [1] * n
         
        # 반으로 나누어서 계산 후 reverse 한걸 붙여서 답으로 낼 예정
        halfArray = math.ceil(n / 2)
        pascalArray = [1] * n
        # n 번 층의 계산을 시작한다
        for i in range(2, n):
            # index 1 ~ 반 까지 계산을 수행한다
            x = 1
            beforeVal = pascalArray[0]
            nowHalfArray = math.ceil((i + 1) / 2)
            while x < nowHalfArray:
                nowVal = pascalArray[x]
                pascalArray[x] += beforeVal
                # 수행하는 계산이 마지막 순번이고 홀수일 때 다음 계산 때 수가 필요하므로
                if i & 1 and x == nowHalfArray - 1:
                    pascalArray[x + 1] = pascalArray[x]
                beforeVal = nowVal
                x += 1
                
        # 홀수 일 경우 배열의 가운데를 제외해야 함
        # 짝수 일 경우 배열을 뒤집어서 만들어야 함
        for i in range(halfArray, n):
            pascalArray[i] = pascalArray[rowIndex - i]
        
        return pascalArray