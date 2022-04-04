# 5525
import sys
input = sys.stdin.readline

n = int(input())
s_n=int(input())
s=input().rstrip()


result=0
cnt=0
i=0
while i < s_n-2:
    if s[i:i+3]!='IOI':
        i+=1
        cnt=0
    else:
        cnt+=1
        i+=2
        if cnt == n:
            result+=1
            cnt-=1
print(result)
