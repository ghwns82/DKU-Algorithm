import sys

N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

dic = {}
for n in Ns:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

for m in Ms:
    if m in dic:
        print(dic.get(m), end=' ')
    else:
        print(0, end=' ')
