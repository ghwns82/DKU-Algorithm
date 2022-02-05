import sys
input=sys.stdin.readline
N=int(input())
count=0
list_=list(map(int, input().split()))
min_=int(max(list_)**0.5)
chk_list=[1]*(max(list_)+1)
chk_list[0]=0
chk_list[1]=0
for i in range(2,min_+1):
    for k in range(i+i,max(list_)+1,i):
        chk_list[k]=0

count=0
for i in range(max(list_)+1):
    if chk_list[i]==1 and i in list_:
        count+=1
print(count)
