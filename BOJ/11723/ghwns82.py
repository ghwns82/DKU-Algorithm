# 11723 집합
import sys
input = sys.stdin.readline
s = [0]*21
for _ in range(int(input())):
    cmd = input().split()
    if len(cmd)==1:
        if cmd[0]=='all':
            s = [1]*21
        else:
            s = [0]*21
    else:
        v = int(cmd[1])
        if cmd[0] == 'check':
            print(s[v])
        elif s[v]:
            if cmd[0]!='add':
                s[v]=0
        else:
            if cmd[0]!= 'remove':
                s[v]=1
