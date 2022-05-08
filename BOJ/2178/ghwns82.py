# 2178
n, m = map(int, input().split())
miro = [list(input()) for _ in range(n)]
work = [(0,0)]
depth = 1
while 1:
    new_work = []
    for x,y in work:
        x,y = int(x), int(y)
        if x == n-1 and y ==m-1:
            break
        if x>=1 and miro[x-1][y]=='1':
            miro[x-1][y]='0'
            new_work.append((x-1,y))
        if y>=1 and miro[x][y-1]=='1':
            miro[x][y-1]='0'
            new_work.append((x,y-1))
        if x<n-1 and miro[x+1][y]=='1':
            miro[x+1][y]='0'
            new_work.append((x+1,y))
        if y<m-1 and miro[x][y+1]=='1':
            miro[x][y+1]='0'
            new_work.append((x,y+1))
    if x == n-1 and y ==m-1:
        break
    work = new_work
    depth+=1
print(depth)
