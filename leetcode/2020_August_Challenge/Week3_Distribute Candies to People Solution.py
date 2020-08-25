'''
Runtime : 24 ms(98.26%)
Memory : 14 MB(30.42%)
수학적인 방법으로 알고리즘을 푸는 것은 어렵지만, 나의 생각으로 구성해보고 싶어 수식을 많이 사용해 보았음.
'''
class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        # 캔디를 1 에서 x 까지 받는 걸 구해야 
        # 캔디 = x(x+1)/2 -> x^2 + x - 2*캔디 = 0
        # x = (-1 + root(1 + 8*캔디)) / 2
        # x 를 int화 하면 소수점을 버린다.
        x = int((-1 + pow((1 + 8 * candies), 0.5)) / 2)
        # 남은 수는 마지막 차례에서 더해줘야 한다.
        left = candies - int(x * (x + 1) / 2)
        
        # x 를 사람 수로 나누었을 때
        # 몫은 배열 전체를 순회하는 횟수를 나타내고
        # 나머지는 배열을 순회하고 멈춘 곳의 인덱스가 된다.
        quotient = x // num_people
        leave = x % num_people
        
        result = [0] * num_people
        for i in range(num_people):
            # a는 순회하여 방문된 횟수
            a = quotient
            # 배열을 순회하다 멈추기 전은 몫 + 1 만큼 더 순회한다.
            if i < leave:
                a += 1
            # 순회된 만큼 (i + 1) 더해지고
            # (순회된 - 1) 만큼 사람수가 등차수열로 증가하므로
            # result[i] = (i + 1) * a + int(a * (a - 1) / 2 * num_people)
            result[i] = int(((i + 1) + (a - 1) / 2 * num_people) * a)
            
        # 마지막 차례에서 더해줄 남은 수
        result[leave] += left
        
        return result