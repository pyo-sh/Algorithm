import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.childs = []

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, numbers):
        head = self.root

        for num in numbers:
            noChild = True
            for child in head.childs:
                if not child.value:
                    return False
                elif child.value == num:
                    head = child
                    noChild = False
                    break
            
            if noChild:
                head.childs.append(Node(num))
                head = head.childs[-1]
        
        if head.childs:
            return False
    
        head.childs.append(Node(None))
        return True

for test in range(int(input())):
    tree = Trie()
    isConsist = True
    for _ in range(int(input())):
        number = input().replace('\n', '')
        if isConsist:
            isConsist = isConsist and tree.insert(number)

    print('YES' if isConsist else 'NO')