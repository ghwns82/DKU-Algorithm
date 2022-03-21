import sys

input= sys.stdin.readline

N=int(input())
list_in=list(map(int, input().split()))
list_in.sort()
M=int(input())
list_out=list(map(int, input().split()))
dict_={}
for i in list_in:
    if i in dict_:
        dict_[i]+=1
    else:
        dict_[i]=1
        
for i in list_out:
    if i in dict_:
        print(dict_[i],end=" ")
    else:
        print(0,end=" ")
        
