'''
Runtime : 64 ms(97.67%)
Memory : 17.1 MB(19.87%)
이 문제는 다른사람이 푼 것을 인용해서 풀었던 것이다..
혼자 힘으로는 풀지 못했었음.
기준을 2중 배열 안의 뒤로 하여 정렬한 뒤 나머지들을 버려주니까 풀렸다
'''

class Solution:
    def eraseOverlapIntervals(self, intervals):
        # 정렬을 x[1] 다음 x[0] 중심으로 하면 x[1]보다 다음 x[0]가 작을 때 범위를 침범한다. 
        line = sorted(intervals, key = lambda x: [x[1], -x[0]])
        
        # 리스트에 아무것도 없을 때 cutLine에 런타임 에러가 뜬다.
        # 또한 길이가 1 아래일 땐 삭제할 게 없다.
        length = len(line)
        if length < 2:
            return 0
        
        cutLine = line[0][1]
        count = 0
        for i in range(1, length):
            if line[i][0] < cutLine:
                count += 1
            else:
                cutLine = line[i][1]
        
        return count