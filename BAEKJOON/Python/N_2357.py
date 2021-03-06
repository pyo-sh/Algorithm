import sys
input = sys.stdin.readline

N, M = map(int, input().split())

garbageNum = (1000000001, 0)
numbers = [int(input()) for _ in range(N)]

# 처음 설정할 때 segment tree 를 구성한다
def init_tree(root, start, end):
    global numbers
    
    if start == end:
        root['value'] = (numbers[start], numbers[start])
        return root['value']
    
    root['left'] = dict()
    root['right'] = dict()

    center = (start + end) // 2
    minimum_1, maximum_1 = init_tree(root['left'], start, center)
    minimum_2, maximum_2 = init_tree(root['right'], center + 1, end)
    root['value'] = (min(minimum_1, minimum_2), max(maximum_1, maximum_2))

    return root['value']

seg_tree = {}
init_tree(seg_tree, 0, N - 1)

# tree 를 통해 값을 구한다
def get_value(root, start, end, scope):
    global garbageNum
    left, right = scope

    # 범위를 벗어나면 그것들은 비교대상에서 없앨 예정이다.
    # 한계점을 반환한다
    if start > right or end < left:
        return garbageNum

    # 범위 안에 있다면 정상적인 범주인 것
    if left <= start and end <= right:
        return root['value']
    
    # 계속 자식 tree 로 파고들기
    center = (start + end) // 2
    minimum_1, maximum_1 = get_value(root['left'], start, center, scope) if 'left' in root else garbageNum
    minimum_2, maximum_2 = get_value(root['right'], center + 1, end, scope) if 'right' in root else garbageNum
    return min(minimum_1, minimum_2), max(maximum_1, maximum_2)

for _ in range(M):
    a, b = map(int, input().split())

    print(' '.join(map(str, get_value(seg_tree, 0, N - 1, (a - 1, b - 1)))))