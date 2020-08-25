'''
Runtime : 36 ms(61.50%)
Memory : 14.2 MB(75.03%)
항상 Recursive 구조는 순환 / 예외 생각 후 조건을 생성하는 방식인 것 같다
'''
# 사용 데이터 구조
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        # 해당 노드가 없으면 0을 반환
        if not root:
            return 0
        
        # 조건에 해당
        if root.left:
            if not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        
        # 일반적인 노드 recursive 진입
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)