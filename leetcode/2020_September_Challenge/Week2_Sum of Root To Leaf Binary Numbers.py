# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travelNode(self, root, bin = 0) -> int:
        if not root:
            return 0
        
        bin = bin << 1
        # shift 가 1이 되어야 한다면..?  +
        if root.val == 1:
            bin += 1
        # 자식이 없을 경우 값을 출력
        if root.left == None and root.right == None:
            return bin
        
        return self.travelNode(root.left, bin) + self.travelNode(root.right, bin)
        
        
    def sumRootToLeaf(self, root) -> int:
        return self.travelNode(root,0)