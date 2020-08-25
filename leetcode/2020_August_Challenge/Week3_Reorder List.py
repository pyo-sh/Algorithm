'''
Runtime : 104 ms(56.31%)
Memory : 23.2 MB(52.24%)
처음의 구상으로는, Runtime이 늘더라도 Memory 사용량을 줄이는 방법으로, LinkedList를 While문으로 반복할 때,
그 안에 LinkedList의 마지막을 찾아 현재 Node의 next로 만드는 방법을 사용했었다.
하지만 Time Limit Exceeded 뜨자마자 바로 배열로 LinkedList Node들을 저장하고
Double Linked List 처럼 접근하여 문제풀이 하였음...
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        pointNode = head
        # 현재의 LinkedList 들의 요소들을 List 로 만들어 뒤에서 부터 접근하게 할 수 있게 함
        reverseList = []
        # 길이는 그냥 필요없을지도 모르지만 변수로 받아서 사용하게했음
        length = 0
        # 요소들을 reverseList 에 넣어줌
        while pointNode:
            reverseList.append(pointNode)
            pointNode = pointNode.next
            length += 1
        
        # reverseList (실제론 그냥 List 순서이지만 접근을 반대로 함)
        pointNode = head
        for i in reversed(range(length)):
            # 현재의 reverseList 와 pointNode가 같다면 (홀수에서 마지막 경우)
            # 현재의 reverseList 와 pointNode.next가 같다면 (짝수에서 마지막 경우)
            # 마무리를 짓고 끝낸다.
            if id(pointNode) == id(reverseList[i]) or id(pointNode.next) == id(reverseList[i]):
                reverseList[i].next = None
                break
            # 다른 경우 마지막의 List를 pointNode.next로 지정한 뒤 다음 반복문으로 넘어간다.
            else:
                reverseList[i].next = pointNode.next
                pointNode.next = reverseList[i]
                pointNode = reverseList[i].next