# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

# bfs 방법으로 트리순회를 하기 위해서 queue 를 가져온다.
# list 로 queue 를 사용한 것 보다 import 하는 것이 효율면에서 좋다고 들었다.
from queue import Queue

class Solution:
    def levelOrderBottom(self, root):
        # 너비로 트리 순회를 하기 때문에 현재 level의 노드 갯수를 가지고 있는 변수가 필요하다.
        nowLevelCount = 1
        # 현재 level의 노드가 가지고 있는 자식 노드의 갯수를 저장하는 변수이다.
        # 다음 level을 순회할 때 필요하게 되는 수이다.
        nextLevelCount = 0
        # 현재 level의 노드들의 val의 값들을 저장하고 있는 list
        levelList = []
        # 결과 값을 저장하는 list 이며 마지막에 reverse 해야 문제에서 원하는 답을 도출해 낼 수 있다
        result = []
        
        # 노드를 queue에 넣어 queue가 빌 때 까지 순회할 예정.
        treeQueue = Queue()
        
        # root 가 null일 경우 그냥 값을 반환해주어야 한다.
        if not root:
            return result
        # 아닐 경우 root 를 queue 에 넣어 알고리즘 시작
        treeQueue.put(root)
        
        while not treeQueue.empty():
            # 노드를 꺼낸 뒤 해야하는 작업
            node = treeQueue.get()
            nowLevelCount -= 1
            levelList.append(node.val)
            
            # 자식 노드들을 queue에 넣는 작업
            if node.left:
                treeQueue.put(node.left)
                nextLevelCount += 1
            if node.right:
                treeQueue.put(node.right)
                nextLevelCount += 1
            
            # 현재 level의 노드를 전부 순회했을 경우 (nowLevelCount == 0)
            if not nowLevelCount:
                nowLevelCount = nextLevelCount
                nextLevelCount = 0
                result.append(list(levelList))
                levelList.clear()
        
        # 결과 값을 원하는 대로 만든 후 반환
        result.reverse()
        return result