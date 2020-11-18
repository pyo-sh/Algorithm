check = True

# 동 서 남 북 왼위 오위 왼아래 오아래 
plusMinus = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]

result = []

while check:
    width, height = map(int, input().split())
    
    if width + height == 0:
        check = False
    
    if width == 0:
        continue
    
    bigMap = [0] * height
    for i in range(height):
        bigMap[i] = input().split()

    count = 0
    stack = []
    for h in range(height):
        for w in range(width):
            if bigMap[h][w] == '1':
                stack.append((w, h))
                while stack:
                    x, y = stack.pop()
                    bigMap[y][x] = '0'

                    for dx, dy in plusMinus:
                        nextX = x + dx
                        nextY = y + dy
                        if 0 <= nextX < width and 0 <= nextY < height:
                            if bigMap[nextY][nextX] == '1':
                                stack.append((nextX, nextY))
                
                count += 1
    
    result.append(count)
    
for count in result:
    print(count)