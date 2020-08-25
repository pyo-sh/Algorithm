'''
Runtime : 100 ms(52.37%)
Memory : 14.4 MB(60.89%)
홀수, 짝수를 구분할 때 1과 AND 연산을 이용해 확인하는 것과 MODULO 연산을 이용하는 것의 차이는 알지만 실제로 구동시간에 영향이 있는지 잘 모르겠다.
소신껏 섞어가며 사용하겠다
'''
class Solution:
    def sortArrayByParity(self, A):
        x = 0
        for i in range(len(A)):
            if not A[i] & 1:
                A[i] , A[x] = A[x] , A[i]
                x += 1
        return A