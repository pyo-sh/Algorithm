class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)
        arr = [0] * (length + 1)
        for num in nums:
            if 0 < num <= length:
                arr[num] = 1
        
        for i in range(1, length + 1):
            if not arr[i]:
                return i
        
        return length + 1