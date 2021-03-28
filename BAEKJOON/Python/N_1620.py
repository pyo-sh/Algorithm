import sys
input = sys.stdin.readline

N, M = map(int, input().split())

book = {}
for i in range(1, N + 1):
    name = input()[:-1]
    book[name] = i
    book[str(i)] = name

for i in range(M):
    string = input()
    if string[-1] == '\n':
        string = string[:-1]
    print(book[string])