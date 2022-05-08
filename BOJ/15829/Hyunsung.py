#15829 Hashing 브론즈 2

import sys
input = sys.stdin.readline

num = int(input())
string = input()
ans = 0

for i in range(num) :
    ans += (ord(string[i]) - 96) * (31 ** i)

print(ans % 1234567891)
