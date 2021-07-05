expressions = input().split('-')

result = sum(map(int, expressions.pop(0).split('+')))
for expr in expressions:
    result -= sum(map(int, expr.split('+')))

print(result)