#1764 듣보잡 실버 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = set()
b = set()
count = 0

for _ in range(N) :
    a.add(input().rstrip())

for _ in range(M) :
    b.add(input().rstrip())

ans = sorted(list(a & b))

print(len(ans))     # 아니 듣보잡의 수를 세는 거래서 M - len(ans) 하고 있었다고... 쥐앤장
for i in ans :
    print(i)