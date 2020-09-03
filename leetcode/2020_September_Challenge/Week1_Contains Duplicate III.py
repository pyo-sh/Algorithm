'''
Runtime: 56 ms(91.01%)
Memory Usage: 16 MB(75.66%)
어려웠다... 처음엔 이중 for문을 이용해서 풀었지만 testcase 10000인 경우에 실패했었음.
비교할 때 나눗셈의 몫을 이용하여 2t이상의 차이나는 숫자들은 비교하지 않게 하고,
Dictionary를 이용하여 비교해 나가는 방법을 사용하였음.
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # 문제에 t의 범위를 안 적어 놨더라...
        # 심지어 testcase에 t가 음수인 경우를 넣어놓아서 넣었음
        if t < 0:
            return False
        
        # 차이나는 크기만큼 나누고 나온 몫이 key, 그 배열이 value가 될 것
        # 나누어서 비교를 하면 2t, 3t 혹은 그 이상의 크기차이부터는 비교를 할 필요가 없다.
        quotient = {}
        # 차이나는 크기가 0 일 때도 있으므로 비교의 범주를 크게 해준다
        size = t + 1
        
        # 하나씩 dictionary에 넣으면서 확인할 것
        for i in range(len(nums)):
            # 차이가 나는 size 만큼의 몫
            numSize = nums[i] // size
            # t + 1 을 해서 나누었기 때문에
            # 같은 몫을 가진 값이 있다면 그것은 차이가 t 아래 만큼 난다는 뜻
            if numSize in quotient:
                return True
            # 나눗셈을 이용했기 때문에 다른 몫을 가져도 오차범위 +- 1 에서 값이 있을 수 있다.
            if numSize - 1 in quotient and nums[i] - quotient[numSize - 1] <= t:
                return True
            if numSize + 1 in quotient and quotient[numSize + 1] - nums[i] <= t:
                return True
            # 위의 해당사항이 없다면 다음 반복문에서 비교를 위한 몫 저장
            quotient[numSize] = nums[i]
            
            # k 만큼의 범위에서 비교를 해야하기 때문에 i 가 k 만큼 된다면 그 전의 값을 제거
            if i >= k:
                del quotient[nums[i - k] // size]
        
        return False
    