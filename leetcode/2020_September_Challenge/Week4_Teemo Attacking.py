class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        count = duration
        poisoned = timeSeries[0]
        for i in range(1, len(timeSeries)):
            count += duration if duration < timeSeries[i] - poisoned else timeSeries[i] - poisoned
            poisoned = timeSeries[i]
        
        return count