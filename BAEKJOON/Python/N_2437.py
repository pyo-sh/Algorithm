import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))

weights.sort()

beforeWeights = 0
for num in weights:
  if beforeWeights + 1 < num:
    break
  beforeWeights += num

print(beforeWeights + 1)