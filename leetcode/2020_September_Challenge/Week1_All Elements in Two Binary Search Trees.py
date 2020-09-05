'''
Runtime: 340 ms(95.66%)
Memory Usage: 17.1 MB(90.24%)
파이썬에서는 어설프게 내가 sort를 직접 하는 것보다
내장된 기능을 사용하는게 더 좋다고 생각할 때가 있다.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        result = []
        stack = []
        if root1:
            stack.append(root1)
        if root2:
            stack.append(root2)
            
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return sorted(result)