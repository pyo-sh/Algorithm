class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        
        n = len(nums) // 3
        result = []
        for i in set(nums):
            if dictionary[i] > n:
                result.append(i)
            
        return sorted(result)
