num = int(input())
string = input().strip()

hashed = 0
for i, char in enumerate(string):
    hashed = (hashed + (ord(char) - 96) * (31 ** i)) % 1234567891

print(hashed)