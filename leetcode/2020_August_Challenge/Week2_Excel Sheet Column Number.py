'''
Runtime : 32 ms(64.53%)
Memory : 13.9 MB(49.60%)
해당 문자를 26진수로 보는 개념으로 풀었다.
'''
import math
class Solution:
    def titleToNumber(self, s):
        # 사용할 변수 선언
        total = 0; length = len(s); i = 0
        
        # String의 길이 만큼 반복
        while i < length:
            # 해당하는 알파벳의 순서
            alphabetNum = ord(s[length - 1 - i]) - 64
            # 26진수와 같은 개념이다?
            total += alphabetNum * int(math.pow(26, i))
            i += 1
            
        return total