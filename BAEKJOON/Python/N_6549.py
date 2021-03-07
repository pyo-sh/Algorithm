import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

# 메모리 초과 떠서 전역 변수로 사용
seg_tree = histogram = []

def init_tree(root, start, end):
    global seg_tree, histogram
    # ! :   처음엔 제일 낮은 높이의 값을 저장했었다.
    #       그렇게 된다면 반으로 나눈 것이 아닌 3 ~ 7 이 넓을 때 그를 탐지할 수 없음
    #   -> 인덱스를 저장해서 그 인덱스에 대해서 또 탐색을 해보자
    if start == end:
        seg_tree[root] = start
    
    else:
        center = (start + end) // 2
        left_index = init_tree(root * 2, start, center)
        right_index = init_tree(root * 2 + 1, center + 1, end)
        seg_tree[root] = left_index if histogram[left_index] < histogram[right_index] else right_index

    return seg_tree[root]

def get_value(root, start, end, scope):
    global seg_tree, histogram
    left, right = scope

    # 범위를 벗어난 query
    if right < start or end < left:
        return -1
    
    # 정상 범주의 query
    if left <= start and end <= right:
        return seg_tree[root]

    # 반으로 계속 쪼개서 맞는 범위를 찾는다
    # ex) 1 ~ 8 but 3 ~ 7
    center = (start + end) // 2
    left_index = get_value(root * 2, start, center, scope)
    right_index = get_value(root * 2 + 1, center + 1, end, scope)

    if left_index == -1:
        return right_index
    elif right_index == -1:
        return left_index
    else:
        return left_index if histogram[left_index] < histogram[right_index] else right_index

def get_max(N, start, end):
    global seg_tree, histogram

    small_index = get_value(1, 0, N - 1, (start, end))

    # 현재 범위에서 가장 낮은 index * 범위 가 넓이이다.
    dimension = (end - start + 1) * histogram[small_index]
    
    # 해당 낮은 index 에서 왼쪽과 오른쪽을 탐색한다.
    left_index = small_index - 1
    if start <= left_index:
        dimension = max(
            dimension, 
            get_max(N, start, left_index)
        )

    right_index = small_index + 1
    if right_index <= end:
        dimension = max(
            dimension,
            get_max(N, right_index, end)
        )
    
    return dimension

while True:
    array = list(map(int, input().split()))
    N = array[0]

    if N == 0:
        break

    histogram = array[1:]

    tree_height = int(math.ceil(math.log2(N))) + 1
    seg_tree = [0] * (2 ** tree_height)
    init_tree(1, 0, N - 1)

    print(get_max(N, 0, N - 1))

    # 메모리 초과 떠서 삭제해줌
    del histogram, seg_tree, tree_height, N