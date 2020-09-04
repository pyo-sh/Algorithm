'''
Runtime: 60 ms(68.68%)
Memory Usage: 13.8 MB(82.57%)
처음에는 문자라서 Tree로 하나하나 비교해나가보다가 Time 초과가 떴다.
그럴 문제가 아니라고 생각해서 Python의 단순 문자열 비교로 풀었다.
깊게 안보고 쉽게 접근했으면 금방 풀릴 문제였을텐데..
'''

class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        
        # 길이가 1 이하이면? 나가리~
        if length <= 1:
            return False
        
        lastCh = s[-1]
        # 마지막 단어와 비교할 것이므로 마지막 단어를 제외한 모두와 비교한다
        for i in range(length - 1):
            # 마지막 단어와 같을 때?
            if s[i] == lastCh:
                # 반복된 횟수(추정) * 지금까지의 문자열 == s 라면 True
                repeatCount = length // (i + 1)
                if s[0:i + 1] * repeatCount == s:
                    return True
        return False