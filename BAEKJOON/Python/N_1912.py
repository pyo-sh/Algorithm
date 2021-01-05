length = int(input())

array = list(map(int, input().split()))

result = array[0]
for i in range(1, length):
    # 1. -와 +를 더해서 0보다 크면 일단 더하는게 이득
    #  => 이때 까지 더한 것 (array[i - 1])이 음수면 안돼...
    if array[i - 1] > 0 and array[i] + array[i - 1] > 0:
        array[i] += array[i - 1]
    
    result = max(result, array[i])

print(result)