import sys

input=sys.stdin.readline

N,K = map(int, input().split())
up_=1
down_=1
for i in range(N-K+1,N+1):
    up_*=i
for i in range(1,K+1):
    down_*=i

print(up_//down_)
