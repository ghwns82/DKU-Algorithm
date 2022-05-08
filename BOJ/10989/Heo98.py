import sys

input=sys.stdin.readline
N=int(input())

list_=[0]*10001
for i in range(N):
    cnt=(int(input()))
    list_[cnt]+=1
for i in range(len(list_)):
    if(list_[i]>=1):
        for k in range(list_[i]):
            print(i)
