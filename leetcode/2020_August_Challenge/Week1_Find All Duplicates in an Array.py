class Solution:
    def findDuplicates(self, nums):
        lst = set(nums)
        for n in nums:
            if n in lst:
                lst.discard(n)
            else:
                lst.add(n)
        return list(lst)