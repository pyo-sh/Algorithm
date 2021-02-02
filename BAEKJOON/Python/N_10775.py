import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

keys = [x for x in range(G + 1)]

length = G

for _ in range(P):
    airplane = int(input())
    index = length
    
    while airplane < keys[index]:
        index -= 1
    
    if keys[index] == 0:
        break
    
    keys.pop(index)

    length -= 1
        
print(G - length)