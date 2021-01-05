class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        history = dict()
        for num in time:
            value = num % 60
            if value in history:
                history[value] += 1
            else:
                history[value] = 1
        
        length = history[0] if 0 in history else 0
        result = length * (length - 1) / 2
        length = history[30] if 30 in history else 0
        result += length * (length - 1) / 2

        for i in range(1, 30):
            if i in history and 60 - i in history:
                result += history[i] * history[60 - i]
        
        return int(result)