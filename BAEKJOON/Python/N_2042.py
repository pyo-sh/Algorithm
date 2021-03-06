import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

numbers = [int(input()) for _ in range(N)]

def init_tree(root, start, end):
    global numbers, seg_tree
    if start == end:
        seg_tree[root] = numbers[start]
        return seg_tree[root]
    
    center = (start + end) // 2
    seg_tree[root] = (
        init_tree(root * 2, start, center)
        + init_tree(root * 2 + 1, center + 1, end)
    )

    return seg_tree[root]

import math
h = int(math.ceil(math.log2(N))) + 1
seg_tree = [0] * (2 ** h)
init_tree(1, 0, N - 1)

def update_tree(root, start, end, index, difference):
    global seg_tree
    # 범위 밖인 애들은 바꾸질 않는다.
    if start > index or index > end:
        return

    seg_tree[root] += difference
    
    # 자식들도 변경해주자
    if start != end:
        center = (start + end) // 2
        update_tree(root * 2, start, center, index, difference)
        update_tree(root * 2 + 1, center + 1, end, index, difference)

def get_value(root, start, end, scope):
    global seg_tree
    left, right = scope

    # 범위를 벗어난다면 구하지 않을 예정이다.
    if start > right or left > end:
        return 0
    
    # 정상 범주 내의 것은 정상 반환
    if left <= start and end <= right:
        return seg_tree[root]
    
    # 자식들의 반환 값을 합하자
    center = (start + end) // 2
    return (
        get_value(root * 2, start, center, scope)
        + get_value(root * 2 + 1, center + 1, end, scope)
    )

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    b -= 1
    if a == 1:
        difference = c - numbers[b]
        update_tree(1, 0, N - 1, b, difference)
        numbers[b] = c
    elif a == 2:
        c -= 1
        print(get_value(1, 0, N - 1, (b, c)))