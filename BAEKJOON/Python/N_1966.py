import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())

    array = list(map(int, input().split()))
    check = [False] * N
    check[M] = True

    count = 0
    while True:
        if array[0] == max(array):
            count += 1
            if check[0]:
                break
            array.pop(0)
            check.pop(0)
        else:
            array.append(array.pop(0))
            check.append(check.pop(0))
        
    print(count)