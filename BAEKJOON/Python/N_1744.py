import sys
input = sys.stdin.readline

N = int(input())
result = 0
numbers = {'pos': [], 'neg': []}
for i in range(N):
  number = int(input())
  if number < 1:
    numbers['neg'].append(number)
  elif number > 1:
    numbers['pos'].append(number)
  else:
    result += number

numbers['pos'].sort()
numbers['neg'].sort(reverse=True)
left_pos = 0
left_neg = 0
while numbers['pos'] or numbers['neg']:
  if numbers['pos']:
    left_pos = numbers['pos'].pop()
    if numbers['pos']:
      result += left_pos * numbers['pos'].pop()
      left_pos = 0
  if numbers['neg']:
    left_neg = numbers['neg'].pop()
    if numbers['neg']:
      result += left_neg * numbers['neg'].pop()
      left_neg = 0

print(result + left_pos + left_neg)