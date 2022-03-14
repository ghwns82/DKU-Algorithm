# 18258
import sys
input = sys.stdin.readline

cur = 0
q = []
for _ in range(int(input())):
    cmd = input().split()
    if len(cmd)==1:
        cmd = cmd[0]
        if cmd == 'pop':
            if cur+1 > len(q):
                print(-1)
            else:
                print(q[cur])
                cur+=1
        elif cmd == 'size':
            print(len(q)-cur)
        
        else:
            if q[cur:cur+1]:
                if cmd == 'empty':
                    print(0)
                elif cmd == 'front':
                    print(q[cur])
                else:
                    print(q[-1])
            else:
                if cmd == 'empty':
                    print(1)
                else:
                    print(-1)
    else:
        q.append(cmd[1])
    
