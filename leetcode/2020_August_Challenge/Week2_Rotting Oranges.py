'''
Runtime : 52 ms(72.84%)
Memory : 13.7 MB(85.63%)
문제 풀이
1. 신선한 오렌지 갯수 확인
2. 썩은 오렌지를 확인
3. 주변의 오렌지를 썩게 만들고 갯수를 줄임
4. 갯수가 그대로이거나 전부 썩으면 종료
반복문을 너무 많이 사용한 것 같아서 좀 더 효울적으로 만들고 싶은 알고리즘 이다.
다른사람의 풀이를 참고해야 할 듯
'''
class Solution:
    def orangesRotting(self, grid):
        count1 = 0
        y = len(grid); x = len(grid[0]) if y else 0
        # Oranges 의 갯수를 알아보자
        for arr in grid:
            count1 += arr.count(1)
        
        count = 0
        beforeLength = 0
        while count1 > 0:
            infection = [0] * x * y; iLength = 0
            for height in range(y):
                for width in range(x):
                    if grid[height][width] == 2:
                        infection[iLength] = [height, width]
                        iLength += 1
            
            if iLength == beforeLength:
                return -1
            
            for i in range(iLength):
                height, width = infection[i]
                if height - 1 >= 0 and grid[height - 1][width] == 1:
                    grid[height - 1][width] = 2
                    count1 -= 1
                    
                if height + 1 < y and grid[height + 1][width] == 1:
                    grid[height + 1][width] = 2
                    count1 -= 1
                
                if width - 1 >= 0 and grid[height][width - 1] == 1:
                    grid[height][width - 1] = 2
                    count1 -= 1
                    
                if width + 1 < x and grid[height][width + 1] == 1:
                    grid[height][width + 1] = 2
                    count1 -= 1
            
            beforeLength = iLength
            count += 1
        
        return count