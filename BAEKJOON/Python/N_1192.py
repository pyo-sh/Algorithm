length = int(input())

house = []
for i in range(length):
    house.append(list(map(int, input().split())))

for i in range(1, length):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

print(min(house[length - 1]))