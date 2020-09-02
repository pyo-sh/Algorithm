'''
Runtime: 36 ms(63.67%)
Memory Usage: 14 MB(17.85%)
순열을 이용해서 데이터를 분류하는 작업만 하는 쉬운 과정을 선택했다.
'''

import itertools

class Solution:
    def largestTimeFromDigits(self, A):
        # 모든 순열 조합을 정한다.
        numbers = list(itertools.permutations(A, 4))
        largestTime = ""
        compareTime = -1
        
        # 순열 조합들 중에서
        for arr in numbers:
            # 시간의 크기를 비교하기 위한 연산
            hour = arr[0] * 600 + arr[1] * 60
            minute = arr[2] * 10 + arr[3]
            # 시간이라 하기에 적합하고
            if hour < 1440 and minute < 60:
                time = hour + minute
                # 최소를 저장한다.
                if time > compareTime:
                    compareTime = time
                    # str로 나타내기 위한 변수
                    largestTime = arr
        # largestTime 이 초기값 ""이 아니라면 값이 있는 것이므로 str로 변경시켜 준다.
        if largestTime:
            largestTime = str(largestTime[0]) + str(largestTime[1]) + ':' + str(largestTime[2]) + str(largestTime[3])
        return largestTime