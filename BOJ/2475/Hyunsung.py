#2475 검증수 브론즈 5

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num_2 = []

for i in num :
    num_2.append(i * i)

print(sum(num_2) % 10)