points = sorted([input().split(' ') for _ in range(int(input()))], key=lambda x: (int(x[1]), int(x[0])))
print(*[p[0] + ' ' + p[1] for p in points], sep="\n")