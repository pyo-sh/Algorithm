import sys
input = sys.stdin.readline

A = input().replace('\n', '')
B = input().replace('\n', '')

comp = input().replace('\n', '')

def get_longest_prefix_suffix(string):
    lps = [0] * len(string)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != string[j]:
            j = lps[j - 1]
        if string[i] == string[j]:
            lps[i] = j
            j += 1

    return lps

def KMP(A, B):
    lps = get_longest_prefix_suffix(B)
    j = 0
    for i in range(len(A)):
        while j > 0 and A[i] != B[j]:
            j = lps[j - 1]
        if A[i] == B[j]:
            if j == (len(B) - 1):
               return True
               #j = lps[j]
            else:
                j += 1

    return False

print('YES' if KMP(A, comp) and KMP(B, comp) else 'NO')