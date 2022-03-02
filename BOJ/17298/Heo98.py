import sys


input=sys.stdin.readline
N=int(input()) # 크기

array_=[]

array_=list(map(int,input().split()))
for i in range(N):
    chk=1
    for k in range(i,N):
        if array_[i]<array_[k]:
            print(array_[k],end=" ")
            chk=0
            break
    if chk==1:
        print('-1',end=" ")






