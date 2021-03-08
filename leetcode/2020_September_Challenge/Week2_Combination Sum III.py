import itertools
class Solution:
    def combinationSum3(self, k, n):
        nums = [i for i in range(1, 10)]
        result = []
        arr = itertools.combinations(nums, k)
        for comb in arr:
            if sum(comb) == n:
                result.append(list(comb))
        
        return result