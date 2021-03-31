import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.childs = []

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, foods):
        
        head = self.root

        while foods:
            food = foods.pop(0)
            
            hasFood = False
            for child in head.childs:
                if child.value == food:
                    head = child
                    hasFood = True
                    break
            
            if not hasFood:
                head.childs.append(Node(food))
                head = head.childs[-1]

    def printTrie(self, root, depth):
        if not root:
            root = self.root

        root.childs.sort(key = lambda x : x.value)

        for child in root.childs:
            print('--' * depth, child.value, sep='')
            self.printTrie(child, depth + 1)

N = int(input())
tree = Trie()
for _ in range(N):
    tree.insert(input().split()[1:])

tree.printTrie(None, 0)