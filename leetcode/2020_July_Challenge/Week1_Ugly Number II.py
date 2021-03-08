class Solution:
    # 2를 곱한 수, 3을 곱한 수, 5를 곱한 수 모두 받아서 가장 낮은 수를 반환
    # 결과 값 : [셋 중 가장 낮은 수, 어떤 수를 곱한 수가 선택 받았는지]
    def minimum(self, two: int, three: int, five: int):
        resultValue = two
        result = 2
        if resultValue > three:
            resultValue = three
            result = 3
        if resultValue > five:
            resultValue = five
            result = 5
        return [resultValue, result]
    
    # ugly number를 구하기
    def nthUglyNumber(self, n: int) -> int:
        # ugly number를 저장하고 있는 배열
        uglyNumber = [1]
        # 배열의 길이를 나타내는 변수
        length = 0
        # ugly number의 index를 나타내는 변수들이며 2의 곱, 3의 곱, 5의 곱을 수행할 ugly number를 나타내는 변수
        # 2, 3, 5 만 곱해서 소인수 분해 시 2, 3, 5 만 남길 예정
        mulOf2 = 0
        mulOf3 = 0
        mulOf5 = 0
        
        # ugly number가 n번째 나올 때 까지 반복
        while length != n - 1:
            # 2, 3, 5를 곱한 수 중 가장 낮은 수를 찾는다
            nextValueList = self.minimum(uglyNumber[mulOf2] * 2, uglyNumber[mulOf3] * 3, uglyNumber[mulOf5] * 5)
            
            # 어떤 수를 구했는지 확인하여 index를 1 추가 시킨다. (다음 곱을 수행시키기 위함)
            if nextValueList[1] == 2:
                mulOf2 += 1
            elif nextValueList[1] == 3:
                mulOf3 += 1
            else:
                mulOf5 += 1
            
            # 만약 곱한 수가 전의 값과 같다면 ex) 2x3, 3x2
            # 이미 결과값이 있으므로 저장하지 않고 다음 수를 계산하기 시작한다
            if uglyNumber[length] == nextValueList[0]:
                continue
            
            # 결과 겂을 저장하여 반영한다.
            uglyNumber.append(nextValueList[0])
            length += 1
        
        # 과연 결과는?
        return uglyNumber[length]