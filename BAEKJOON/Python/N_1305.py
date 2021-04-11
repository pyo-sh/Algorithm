import sys
input = sys.stdin.readline

L = int(input())
string = input()
if string[-1] == '\n':
    string = string[:-1]

lps = [0] * len(string)
j = 0
for i in range(1, len(string)):
    while j > 0 and string[i] != string[j]:
        j = lps[j - 1]
    if string[i] == string[j]:
        j += 1
        lps[i] = j

print(L - lps[-1])
