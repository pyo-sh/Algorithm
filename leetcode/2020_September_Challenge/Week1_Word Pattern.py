'''
Runtime: 32 ms(60.84%)
Memory Usage: 14 MB(7.79%)
'''

class Solution:
    def wordPattern(self, pattern: str, str: str):
        history = {}
        overlap = set()
        words = str.split(' ')
        
        if not len(pattern) == len(words):
            return False
        
        # enumerate 는 index 와 value 모두 가지고 싶을 때 사용하면 좋다.
        for i, ch in enumerate(pattern):
            if ch in history:
                if not history[ch] == words[i]:
                    return False
            else:
                if words[i] in overlap:
                    return False
                history[ch] = words[i]
                overlap.add(words[i])
                
        return True