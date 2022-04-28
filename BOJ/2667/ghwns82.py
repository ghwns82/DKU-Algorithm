from collections import deque

n = int(input())
matrix = [list(input()) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='1':
            cnt=0
            work= deque([(i,j)])
            while work:
                x,y = work.popleft()
#                 print('xy', (x,y), 'start', (i,j))
                if matrix[x][y]=='1':
                    cnt+=1
                    matrix[x][y]=False
                    if y<(n-1) and matrix[x][y+1]=='1':
                        work.appendleft((x,y+1))
                    if x<(n-1) and matrix[x+1][y]=='1':
                        work.appendleft((x+1,y))
                    if 0<y and matrix[x][y-1]=='1':
                        work.appendleft((x,y-1))
                    if 0<x and matrix[x-1][y]=='1':
                        work.appendleft((x-1,y))
#                 print('work', work, 'cnt', cnt)
            result.append(cnt)
print(len(result))
result.sort()
print(*result, sep='\n')
