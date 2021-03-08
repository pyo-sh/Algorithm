class Solution(object):
    def largestOverlap(self, A, B):
        best = 0; movedA = 0; movedB = 0
        length = len(A)
        for moveRow in range(length):
            for moveCol in range(length):
                for i in range(0, length - moveRow):
                    for j in range(0, length - moveCol):
                        if A[i + moveRow][j + moveCol] and B[i][j]:
                            movedA += 1
                        if A[i][j] and B[i + moveRow][j + moveCol]:
                            movedB += 1
                best = max(best, movedA, movedB)
                movedA = 0
                movedB = 0
        return best