import sys

input=sys.stdin.readline
N=int(input())
list_=[int(input()) for i in range(N)]
list_.sort()
for i in range(N):
    print(list_[i])
