import sys

input=sys.stdin.readline
N=int(input())

list_=[]
for i in range(N):
    x,y=map(int, input().split())
    list_.append([x,y])

list_.sort(key= lambda x: x[1])
list_.sort(key= lambda x : x[0])

for i in range(N):
    print(list_[i][0], end=" ")
    print(list_[i][1])

