class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        # gas - cost 를 모아놓은 변수. 음수이면 무조건 -1 이 된다
        total = 0
        # 현재 진행중인 gas - cost (순환으로 알아야 하기 때문)
        nowGas = 0
        result = 0
        
        for i in range(length):
            nowGas += gas[i] - cost[i]
            # 못가면? 다음 차례를 해답으로 보고 total은 지나온 곳의 남은 gas
            if nowGas < 0:
                result = i + 1
                total += nowGas
                nowGas = 0
        # 총 -1 일 경우... 안됨
        # for문 돌면서 result로 남긴 곳이 답
        total += nowGas
        if total < 0:
            return -1
        else:
            return result