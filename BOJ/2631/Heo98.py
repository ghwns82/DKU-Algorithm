import sys

input=sys.stdin.readline

N=int(input())
li_=[]
for _ in range(N):
    li_.append(int(input()))

dp_=[1]*N
max_count=0

for i in range(N):
    for j in range(i):
        if li_[j]<li_[i]:
            if dp_[i]<dp_[j]+1:
                dp_[i]=dp_[j]+1
print(N-max(dp_))


