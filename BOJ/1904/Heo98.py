import sys

input=sys.stdin.readline

N=int(input())
list_=[0]*(N+1)
for i in range(0,N+1):
    if i==0 or i==1:
        list_[i]=1
    else:
        list_[i]=(list_[i-2]+list_[i-1])%15746
    

print(list_[N])
