import sys
from collections import Counter

input=sys.stdin.readline


test_num=int(input())

for i in range(test_num):
    num=int(input())
    list_=[]
    for k in range(num):
        a,b=input().split()
        list_.append(b)
    res_1=1
    result=Counter(list_)
    for key in result:
        res_1*=result[key]+1
        
    print(res_1-1)


