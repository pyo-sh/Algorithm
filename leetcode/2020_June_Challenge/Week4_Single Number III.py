class Solution:
    def singleNumber(self, nums):
        lst = set()
        for n in nums: 
            if n in lst:
                lst.discard(n)
            else: lst.add(n)
        return list(lst)