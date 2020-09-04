'''
Runtime: 32 ms(97.19%)
Memory Usage: 13.8 MB(69.55%)
처음에는 앞, 뒤의 크기를 지정해서 비교를 했다.
하지만 다른 사람의 코드를 참고하고 난 뒤, for문을 이용해 앞의 크기를 저장할 필요 없이 겹치는 영역을 확인할 수 있었다.
메모리를 비약적으로 줄일 수 있었다.
런타임 면에서는 같은 O(n) 이라서 차이가 별로 없는 듯...
'''

class Solution:
    def partitionLabels(self, S):
        history = {}
        length = len(S)
        
        for i in range(length):
            history[S[i]] = i
        
        result = []
        count = 0
        setting = -1
        for i in range(length):
            # 처음이나 잘라내고 난 뒤에 지정을 해줘야함.
            if setting == -1:
                setting = history[S[i]]
            # 현재보다 전의 선택된 마지막 문자가 클 때
            if i < setting:
                # 그 범주 안에서 다른 뒤의 문자가 나오면 setting 을 업데이트
                if setting < history[S[i]]:
                    setting = history[S[i]]
            # 현재 문자가 마지막 문자보다 크다면 그것은 잘라내야 하는 것
            else:
                # 마지막 문자 위치 - 현재까지의 갯수 가 답이다.
                result.append(setting + 1 - count)
                # 현재까지의 갯수를 count
                count += result[-1]
                # 초기 상태로 지정
                setting = -1
                
        return result