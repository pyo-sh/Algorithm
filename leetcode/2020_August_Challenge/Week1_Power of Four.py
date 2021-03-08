class Solution:
    def isPowerOfFour(self, num: int):
        # 음수는 4의 제곱수가 아니다.
        if num < 0:
            return False
        
        binNum = bin(num)
    
        # 4의 제곱수는 이진수로 1이 하나밖에없다.
        if binNum.count('1') != 1:
            return False
        # (len(binNum) - 2(0b)는 이진수의 길이
        # binNum.find - 1 는 현재 1의 위치
        # 이진수의 길이 - 현재 1의 위치 = 뒤의 0의 갯수
        elif (len(binNum) - binNum.find('1') - 1) % 2 != 0:
            return False
        
        return True