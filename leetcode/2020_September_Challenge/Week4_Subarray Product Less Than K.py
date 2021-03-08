class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        count = 0
        product = 1
        rear = 0
        
        for front in range(len(nums)):
            product *= nums[front]
            while product >= k and rear <= front:
                product //= nums[rear]
                rear += 1
            if product < k and rear <= front:
                count += front - rear + 1
            
        return count