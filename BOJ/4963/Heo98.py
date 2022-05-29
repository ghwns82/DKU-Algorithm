import sys
sys.setrecursionlimit(10**6)
def dfs(y,x):
    if x<0 or x>=w or y<0 or y>=h:
        return False
    
    if island[y][x] == 1:
        #방문처리
        island[y][x] = 0
        # 상하좌우 탐색
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        # 대각선 탐색
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True
    return False

input= sys.stdin.readline

while(1):
    w,h=map(int,input().split())
    
    if w ==0 and h == 0:
        break
    island=[]
    for _ in range(h):
        island.append(list(map(int,input().split())))
    result=0
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                result+=1
    print(result)
