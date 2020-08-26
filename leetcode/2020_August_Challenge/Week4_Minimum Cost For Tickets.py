'''
Runtime : 88 ms(11.99%)
Memory : 14 MB(34.67%)
Dynamic Programming을 처음에 떠올리지 못했다.
계속 연습할 것
하루, 일주일, 한달 을 기준으로 가장 좋은 것을 고르는 것이였는데
하루라는 단위 덕분에 계속해서 비교를 해도 되었던 것 같다.
'''

class Solution:
    def mincostTickets(self, days, costs):
        # dynamic programming 배열은 인덱스의 날에 사용된 비용들을 저장하고 있음
        dp = [0] * (days[-1] + 1)
        # 시간이 지날수록 얼만큼의 비용이 드는지 확인하는 반복문
        for i in range(days[-1] + 1):
            # 만약 여행을 하지 않는 날이라면? 비용은 그대로 일 것이다.
            if i not in days:
                dp[i] = dp[i - 1]
            # 여행이 하루 걸리는 날이 cost가 생기므로 7일, 30일을 비교하며 비용계산을 할 수 있다.
            # max를 사용하는 이유 : - 연산을 사용하기 때문에 index 가 음수가 되지 않게 하기 위함
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2]
                           )
        # 마지막 날에 사용된 비용을 계산한다.
        return dp[-1]