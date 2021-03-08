class Solution:
    def findTheDifference(self, s, t):     
        check = set()
        for ch in s + t:
            if ch in check:
                check.discard(ch)
            else:
                check.add(ch)
        return check.pop()