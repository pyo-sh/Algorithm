import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n + 1)
for i, num in enumerate(inorder):
    position[num] = i

def preorder(in_range, post_range):
    global inorder, postorder, position
    if in_range[0] > in_range[1] or post_range[0] > post_range[1]:
        return
    
    root = postorder[post_range[1]]
    print(root, end = ' ')

    left_size = position[root] - in_range[0]

    preorder((in_range[0], position[root] - 1), (post_range[0], post_range[0] + left_size - 1))
    preorder((position[root] + 1, in_range[1]), (post_range[0] + left_size, post_range[1] - 1))

preorder((0, n-1), (0, n-1))