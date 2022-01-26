# 10845

from collections import deque

import sys
input = sys.stdin.readline

que = deque([])
for _ in range(int(input())):
    if (cmd:=input().split())[0]=="push":
        que.append(cmd[1])
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        print(int(len((que))<=0))
    else:
        if not que:
            print(-1)
        elif cmd[0] == "pop":
            print(que.popleft())
        elif cmd[0] == "back":
            print(que[-1])
        else:
            print(que[0])
