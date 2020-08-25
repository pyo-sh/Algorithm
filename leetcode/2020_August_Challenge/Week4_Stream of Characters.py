'''
Runtime : 704 ms(80.23%)
Memory : 38.7 MB(51.43%)
Python으로 다른 언어처럼 Tree Class를 작성하다가 Dictionary를 이용해 Tree 처럼 작성할 수 있음을 알 수 있었다.
'''
# 이때까지 query로 받아온 문자들을 문자열의 뒤에서 부터 검사해야 한다.
# 'ababc' 를 a <- b <- a <- b <- c 로 Tree로 저장하여 비교를 쉽게 하기 위해 트리 생성
class StreamChecker:
    def __init__(self, words):
        # 받은 배열에서 단어들의 tree를 dictinary로 저장할 것임.
        # (같은 단어면 같은 뿌리를 가지도록)
        self.treeNode = {}
        # query를 통해 입력해온 단어들을 저장할 것임.
        self.history = ""
        
        # words의 트리를 self.words에 넣는다.
        for word in words:
            # 처음엔 tree의 root를 현재의 노드로 지정해주기 위함 
            currentNode = self.treeNode
            # 마지막 단어부터 넣어야 비교가 쉽다.
            for letter in word[::-1]:
                # dictionary 안에 단어가 없다면 새로운 dictionary를 추가하여 오류 방지
                if letter not in currentNode:
                    currentNode[letter] = {}
                # dictionary 안에 넣습니다.
                currentNode = currentNode[letter]
            # 마지막임을 알려주는 단어를 넣어 단어의 끝을 확인
            currentNode['END'] = {} 
        
    def query(self, letter):
        # 나중에 들어온 단어가 먼저 비교되어야 한다.
        # 그래서 self.history += letter 을 안했다.
        self.history = letter + self.history
        
        currentNode = self.treeNode
        # 현재 가지고 있는 tree들과 query를 통해 입력해온 단어들의 tree를 비교
        for historyLetter in self.history:
            # dictionary 안에 없다? 모든 단어와 같지 않다는 뜻이다.
            if historyLetter not in currentNode:
                return False
            
            # tree는 다음으로 넘어간다.
            currentNode = currentNode[historyLetter]
            
            # 단어의 마지막 까지 왔다 = 단어와 같다 
            if 'END' in currentNode:
                return True
            
        return False