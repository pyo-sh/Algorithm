'''
Runtime : 28 ms(97.22%)
Memory : 14 MB(63.50%)
h-index란?
어떤 사람의 h번 이상 인용된 논문이 h개 일 때 이를 h-index라고 한다.
정렬 후 문제 풀이를 하니 어려움은 없었다.
'''
class Solution:
    def hIndex(self, citations):
        # 배열에서 내림차순으로 정렬한 뒤 갯수를 확인하며 비교할 예정
        citations.sort(reverse = True)
        count = 0
        for i in citations:
            # 갯수가 수를 뛰어넘는 순간의 갯수가 h-index가 되므로
            if i <= count:
                return count
            count += 1
        return count