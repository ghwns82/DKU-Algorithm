import sys
input=sys.stdin.readline

start,end=(map(int,input().split()))
prime_list=[True]*(end+1)

# end의 최대 약수가 sqrt(end) 이하이므로 i=sqrt(end)까지 검사
min_= int(end**0.5)
if start==1: start=2
for i in range(2,min_+1):
    if prime_list[i]==True:
        for j in range(i+i,end+1,i):
            prime_list[j]=False


print('\n'.join(str(i) for i in range(start,end+1) if prime_list[i]==True))

