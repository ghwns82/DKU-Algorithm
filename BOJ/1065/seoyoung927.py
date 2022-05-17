# 1065, 한수, Silver 4
# https://www.acmicpc.net/problem/1065

import sys

N=int(sys.stdin.readline())

def is_hansu(n):
    if(n<100):
        return True
    
    #100
    #012
    #len=3
    #0,1
    tmp=str(n)
    for i in range(len(tmp)-2):
        n1=int(tmp[i])
        n2=int(tmp[i+1])
        n3=int(tmp[i+2])
        if((n1-n2)!=(n2-n3)):
            return False

    return True

cnt=0
for i in range(1, N+1, 1):
    if(is_hansu(i)):
        cnt+=1

print(cnt)
