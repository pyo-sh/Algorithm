import sys
input = sys.stdin.readline

# isZero 는 0 / 1을 구별
# count 는 삭제할 때 참고하게 될 것
# 이진 트리의 모습을 갖출 것이다.
class Node:
    def __init__(self, value):
        self.isZero = value
        self.count = 1
        self.left = None
        self.right = None

class Trie:
    def __init__(self):
        self.root = Node(None)
    # 0과 1로 이루어진 값을 Trie 로 저장
    # 저장할 때마다 count 값을 ++ 
    def insert(self, binary):
        head = self.root

        for num in binary:
            isZero = (num == '0')
            child = head.left if isZero else head.right
            if child:
                child.count += 1    
            else:
                child = Node(isZero)
                if isZero:
                    head.left = child
                else:
                    head.right = child
            head = child
    # count 값을 감소시킨다.
    # count 값이 0이라면 그 자식들도 다 0이므로 삭제시키는 일
    def delete(self, binary):
        head = self.root

        for num in binary:
            isZero = (num == '0')
            child = head.left if isZero else head.right
            child.count -= 1
            if not child.count:
                if isZero:
                    head.left = None
                else:
                    head.right = None
            head = child
    # 상위에서부터 xor 하여 1이 나오는 것을 선택 (없다면 0)
    def operate(self, binary):
        head = self.root

        result = '0b'
        for num in binary:
            isZero = (num == '0')
            if (head.right and isZero) or not head.left:
                child = head.right
            else:
                child = head.left
            
            result += '0' if child.isZero == isZero else '1'
            head = child
        
        print(int(result, 2))

# 함수 접근을 위한 배열
func = ['', 'insert', 'delete', 'operate']

tree = Trie()
# 10의 9승은 2진수 30자리다.
tree.insert(''.zfill(30))
for _ in range(int(input())):
    op, value = map(int, input().split())
    value = format(value, 'b').zfill(30)
    getattr(tree, func[op])(value)