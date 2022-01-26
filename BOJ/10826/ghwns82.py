# 10828

import sys
input = sys.stdin.readline
stack=[]
for _ in range(int(input())):


    if (cmd:=input().split())[0]=="push":
        stack.append(cmd[1])

    elif cmd[0] =="size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(int(len((stack))<=0))
    else:
        if not stack:
            print(-1)
        elif cmd[0] == "pop":
            print(stack.pop())
        else:
            print(stack[-1])
