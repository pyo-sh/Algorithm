string_1 = input()
string_2 = input()

length_1 = len(string_1) + 1
length_2 = len(string_2) + 1

history = [[0] * length_2 for col in range(length_1)]

for i in range(1, length_1):
    for j in range(1, length_2):
        if string_1[i - 1] == string_2[j - 1]:
            history[i][j] = history[i - 1][j - 1] + 1
        else:
            history[i][j] = max(history[i - 1][j], history[i][j - 1])

print(history[length_1 - 1][length_2 - 1])