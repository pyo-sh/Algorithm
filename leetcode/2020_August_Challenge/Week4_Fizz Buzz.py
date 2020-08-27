'''
Runtime : 24 ms(100.00%)
Memory : 14.8 MB(79.52%)
문제 정말 쉬웠다. Modulo 연산 사용 안하려고 노력했다
'''
class Solution:
    def fizzBuzz(self, n):
        result = [str(x) for x in range(1, n + 1)]
        
        if n >= 3:
            for i in range(2, n, 3):
                result[i] = 'Fizz'
        
        if n >= 5:
            for i in range(4, n, 5):
                if result[i] == 'Fizz':
                    result[i] += 'Buzz'
                else:
                    result[i] = 'Buzz'
        
        return result