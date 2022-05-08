#10845 큐 실버 4

import sys
input = sys.stdin.readline

N = int(input())
Q = []
top = 0

for i in range(N) :
    command = input().split()

    if command[0] == 'push' :
        Q.append(command[1])
    
    elif command[0] == 'pop' :
        if len(Q) - top != 0 :
            print(Q[top])
            top += 1
        else : 
            print(-1)

    elif command[0] == 'size' :
        print(len(Q) - top)
    
    elif command[0] == 'empty' :
        if len(Q) - top == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == 'front' :
        if len(Q) - top != 0 :
            print(Q[top])
        else : 
            print(-1)

    elif command[0] == 'back' :
        if len(Q) - top != 0 :
            print(Q[-1])
        else : 
            print(-1)