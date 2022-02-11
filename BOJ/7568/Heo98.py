import sys

input=sys.stdin.readline
N=int(input())
N_list=[]
for i in range(N):
    x,y=map(int,input().split())
    N_list.append([x,y])

for i in N_list:
    count=1
    for j in N_list:
        if i[0]<j[0] and i[1]<j[1]:
            count+=1
    print(count,end=" ")
