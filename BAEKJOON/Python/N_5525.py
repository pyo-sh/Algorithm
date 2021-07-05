N = int(input())
M = int(input())

string = input()
check = [False] * M

for i in range(2, M):
    if string[i - 2] == 'I' and string[i - 1] == 'O' and string[i] == 'I':
        check[i - 2] = True

result = 0
odd = 0
even = 0
for i in range(0, M , 2):
    if check[i]:
        odd += 1
        if odd >= N:
            result += 1
    else: odd = 0
    if i + 1 < M and check[i + 1]:
        even += 1
        if even >= N:
            result += 1
    else: even = 0

print(result)