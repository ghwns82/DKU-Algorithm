#소트인사이드
import sys

N=int(sys.stdin.readline())

llist=[]
while(N>0):
    llist.append(N%10)
    N=N//10
llist=sorted(llist)

result=0
tmp=1
for i in llist:
    result+=i*tmp
    tmp*=10

print(result)
