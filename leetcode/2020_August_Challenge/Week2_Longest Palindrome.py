'''
Runtime : 28 ms(85.32%)
Memory : 13.8 MB(69.45%)
어려움은 없던 문제
'''
class Solution:
    def longestPalindrome(self, s):
        out = odd = 0
        for i in set(s):
            out += s.count(i)
            if s.count(i) % 2==1:
                odd += 1
        return out if odd == 0 else out - odd + 1