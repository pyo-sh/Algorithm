class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        entire =  1
        # 계단의 수를 넘어가면 반복문이 끝난다.
        while entire <= n:
            k += 1
            entire += k
        
        # 다음 계단의 수까지 계산한 후 반복문이 끝나므로 -1을 해주어야 한다.
        return k - 1
        
        # 다른 방법
        # k(k+1) <= 2n
        # k^2 + k + (1/4) <= 2n + (1/4)
        # k <= root(2n + (1/4)) - (1/2)
        # return int((2 * n + 0.25) ** 0.5 - 0.5)