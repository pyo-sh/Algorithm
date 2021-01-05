# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.history = TreeNode()
        self.curr = self.history

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def in_order(root):
            if root:
                in_order(root.left)
                self.curr.right = TreeNode(val=root.val)
                self.curr = self.curr.right
                in_order(root.right)
        in_order(root)
        return self.history.right