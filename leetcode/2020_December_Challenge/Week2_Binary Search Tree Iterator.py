class BSTIterator:
    def __init__(self, root: TreeNode):
        self.length = 0
        self.now = 0
        self.in_order = []
        self.setNode(root)
    
    def setNode(self, node):
        if node.left:
            self.setNode(node.left)
        
        self.in_order.append(node.val)
        self.length += 1

        if node.right:
            self.setNode(node.right)

    def next(self) -> int:
        if self.now < self.length:
            self.now += 1
            return self.in_order[self.now - 1]
        
    def hasNext(self) -> bool:
        return True if self.now < self.length else False