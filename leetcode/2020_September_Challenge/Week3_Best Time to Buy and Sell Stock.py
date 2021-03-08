class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if not length:
            return 0
        
        maxCost = 0
        minNum = prices[0]
        for i in range(1, length):
            maxCost = max(maxCost, prices[i] - minNum)
            minNum = min(minNum, prices[i])
            
        return maxCost