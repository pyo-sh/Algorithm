import sys
input = sys.stdin.readline

string = input().replace('\n', '')
exp = input().replace('\n', '')

if len(string) < len(exp):
    print(string)

result = []

for i in range(len(string)):
    result.append(string[i])

    if string[i] == exp[-1] and len(result) >= len(exp):
       length = len(result) - len(exp)
       if ''.join(result[length:]) == exp:
           del result[length:]

if result:
    print(''.join(result))
else:
    print('FRULA')