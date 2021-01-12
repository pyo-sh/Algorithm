import sys
input = sys.stdin.readline
day, cake = map(int, input().split())

# 첫날이 a, 두번째날이 b면
# a, b가 피보나치 수인
# 2차 방정식이 나오더라... 경우의 수로 풀어봤다
a = 1
b = 1
for i in range(3, day):
    a, b = b, a + b

x = 1
a_x = a * x
while a_x < cake:
    quotient = (cake - a_x) // b
    remainder = (cake - a_x) % b
    if remainder == 0 and x < quotient:
        print(x)
        print(quotient)
        break
    x += 1
    a_x = a * x