import sys
input = sys.stdin.readline

A, B = map(int, input().split())

string = str(A // B)
A = A % B
if not A == 0:
    string += '.'

place = 0
while A != 0 and place < 1003:
    A *= 10
    string += str(A // B)
    A = A % B
    place += 1

print(string)