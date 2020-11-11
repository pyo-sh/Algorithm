class Solution:
    def uniquePathsIII(self, grid):
        yLength = len(grid)
        if not yLength:
            return 0
        xLength = len(grid[0])
        if not xLength:
            return 0
        
        result = 0
        # 모든 0을 밟아야 하므로 0의 갯수를 알아야 한다.
        # 1을 둔 이유는 history에 start point도 포함될것이기 때문
        count = 1
        # 새로 안 사실
        # 파이썬의 변수들 중 List 와 Dict를 제외하고는 전부 immutable이다.
        # -> 튜플, 문자열, 정수 등등은 지역변수로 선언되더라도 밖의 함수에서 참조가 가능
        # -> 이 값을 변경하고 싶다면 nonlocal 을 사용한다. (추천되지 않는 사항)
        for i in range(yLength):
            for j in range(xLength):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    start = (j, i)
                elif grid[i][j] == 2:
                    end = (j, i)
        
        def dfs(point, history):
            x, y = point
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                currentX = x + dx
                currentY = y + dy
                # 참조할 수 있는 x, y 인지?
                if 0 <= currentX < xLength and 0 <= currentY < yLength:
                    # 이미 들렸거나 (history에 있거나) 벽 인 경우 갈 수 없다는 것을 확인
                    if (currentX, currentY) not in history and grid[currentY][currentX] != -1:
                        # 혹시 마지막 이신가요...?
                        if (currentX, currentY) == end:
                            # 모든 0을 밟아야 한다 했으므로 count에 맞아야 한다.
                            if len(history) == count:
                                # 바깥 함수의 값을 건드리려면 nonlocal을 사용하래
                                nonlocal result
                                result += 1
                        # 아니면 더 미로를 도세요
                        else:
                            # 튜플 값은 바꿀 필요가 없어서 얕은 복사로도 가능
                            # -> 각 history가 다를 것
                            dfs((currentX, currentY), history + [(currentX, currentY)])
        dfs(start, [start])
        return result