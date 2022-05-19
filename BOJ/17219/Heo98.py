import sys

input=sys.stdin.readline

N,M=map(int,input().split())
dict_={}

for _ in range(N):
    key_,value_=map(str,input().split())
    dict_[key_]=value_

for _ in range(M):
    what=input().strip()
    print(dict_[what])
