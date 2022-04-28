import sys
input = sys.stdin.readline
#7562
for _ in range(int(input())):
    n=int(input())
    chess = [[-1]*n for i in range(n)]
    work = [list(map(int, input().split()))]
    goal_x, goal_y = map(int, input().split())
    if work[0] == [goal_x, goal_y]:
        print(0)
        continue
    depth=1
    done = False
    while work:
        new_work=[]
        for x,y in work:
            for a,b in [(x-1,y-2), (x-2,y-1), (x+1,y-2), (x+2,y-1), (x-1,y+2), (x-2,y+1), (x+1,y+2), (x+2,y+1) ]:
                if a== goal_x and b == goal_y:
                    done = True
                    print(depth)
                    break
                if 0<=a<n and 0<=b<n and chess[a][b]==-1:
                    chess[a][b] = depth
                    new_work.append((a,b))
            if done:
                break
        if done:
            break
        work = [*new_work]
        depth+=1
