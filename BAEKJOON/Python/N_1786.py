import sys
input = sys.stdin.readline

text = input().replace('\n', '')
pattern = input().replace('\n', '')

# Longest Prefix & Suffix
lps = [0] * len(pattern)
j = 0
for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
        j = lps[j - 1]
    if pattern[i] == pattern[j]:
        lps[i] = j = j + 1

# get Pattern from Text
result = []
j = 0
for i in range(len(text)):
    # if it doesn't match, makes algorithm better
    while j > 0 and text[i] != pattern[j]:
        j = lps[j - 1]
    # check the pattern
    if text[i] == pattern[j]:
        if j == (len(pattern) - 1):
            result.append(i - len(pattern) + 1 + 1)
            j = lps[j]
        else:
            j += 1

print(len(result), ' '.join(map(str, result)), sep= '\n')