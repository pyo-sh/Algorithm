class Solution:
    def rob(self, nums) -> int:
        length = len(nums)
        if length < 3:
            return max(nums) if nums else 0
        
        dp = [0] * (length)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]