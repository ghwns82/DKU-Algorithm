import sys

input=sys.stdin.readline

N, M=map(int, input().rstrip().split())

pocket_={}
for i in range(1,N+1):
    name=input().rstrip()
    pocket_[name]=str(i)
    pocket_[str(i)]=name
for i in range(M):
    what_=input().rstrip()
    print(pocket_[what_])
