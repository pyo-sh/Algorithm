import sys
input = sys.stdin.readline

lps = []
def get_longest_prefix_suffix(string):
    global lps
    lps = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = lps[j - 1]
        if string[i] == string[j]:
            j += 1
            lps[i] = j

def KMP(A, B):
    global lps
    result = []
    j = 0
    for i in range(len(A)):
        while j > 0 and A[i] != B[j]:
            j = lps[j - 1]
        if A[i] == B[j]:
            if j == (len(B) - 1):
                result.append(i - len(B) + 1)
                j = lps[j]
            else:
                j += 1

    return len(result)

N = int(input())

for _ in range(N):
    order_string = input().replace('\n', '')

    order = dict()
    order_length = len(order_string)
    for index, char in enumerate(order_string):
        order[char] = index
    order_string = order_string + order_string

    text = input().replace('\n', '')
    get_longest_prefix_suffix(text)

    cipher = input().replace('\n', '')

    result = []
    if KMP(cipher, text) == 1:
        result.append('0')
    for shift in range(1, order_length):
        compare = []
        for char in text:
            compare.append(order_string[order[char] + shift])
        if KMP(cipher, ''.join(compare)) == 1:
            result.append(str(shift))
    
    if len(result) == 0:
        print('no solution')
    elif len(result) == 1:
        print('unique:', result[0])
    else:
        print('ambiguous:', ' '.join(result))