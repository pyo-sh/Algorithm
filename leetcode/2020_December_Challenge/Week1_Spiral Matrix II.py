class Solution:
    def generateMatrix(self, n: int):
        result = [[0] * n for _ in range(n)]
        D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dx, dy = 0, 1
        x = y = k = 0
        for i in range(1, n * n + 1):
            result[x][y] = i
			# if cannot go further on current direction, turn right
            if not (0 <= x + dx < n and 0 <= y + dy < n and result[x + dx][y + dy] == 0):
                k = (k + 1) % 4
                dx, dy = D[k]
            x += dx
            y += dy
        return result
            