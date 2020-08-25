'''
Runtime : 24 ms(96.07%)
Memory : 13.9 MB(35.97%)
어려움을 느낀 점은 없지만, Python이 아니였을 때 in을 사용하지 않고서 알고리즘을 효율적으로 활용할 방법을 모색해보고 싶다.
'''
class Solution:
    def toGoatLatin(self, S):
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        splited = S.split(' ')
        
        for i in range(len(splited)):
            word = splited[i]
            if word[0] not in vowel:
                word = word[1:] + word[0]
            splited[i] = word + 'ma' + ('a' * (i + 1))
        
        return ' '.join(splited)