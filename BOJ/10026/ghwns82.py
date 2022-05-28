# 10026
from copy import deepcopy
n = int(input())
matrix= [list(input()) for _ in range(n)]


matrix2 = deepcopy(matrix)
visited = [[False]*n for i in range(n)]
work=[]
cnt_b=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt_b+=1
            visited[i][j]=True
            crt = matrix[i][j]
            if crt != 'B':
                matrix2[i][j]='R'
            work.append((i,j))
#             print('start',(i,j), crt)
            while work:
#                 print(work)
                new_work=[]
                for x,y in work:
                    a,b=x, y-1
                    if b>=0 and not visited[a][b] and matrix[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                        if crt != 'B':
                            matrix2[a][b]='R'
                    a,b = x, y+1
                    if b<n and not visited[a][b] and matrix[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                        if crt != 'B':
                            matrix2[a][b]='R'
                    a,b = x-1,y
                    if a>=0 and not visited[a][b] and matrix[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                        if crt != 'B':
                            matrix2[a][b]='R'
                    a,b = x+1, y
                    if a<n and not visited[a][b] and matrix[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                        if crt != 'B':
                            matrix2[a][b]='R'
                work = new_work
print(cnt_b, end = ' ')
work=[]
cnt_b=0
visited = [[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt_b+=1
            visited[i][j]=True
            crt = matrix2[i][j]
            if crt != 'B':
                matrix2[i][j]='R'
            work.append((i,j))
#             print('start',(i,j), crt)
            while work:
#                 print(work)
                new_work=[]
                for x,y in work:
                    a,b=x, y-1
                    if b>=0 and not visited[a][b] and matrix2[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                    a,b = x, y+1
                    if b<n and not visited[a][b] and matrix2[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                    a,b = x-1,y
                    if a>=0 and not visited[a][b] and matrix2[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                    a,b = x+1, y
                    if a<n and not visited[a][b] and matrix2[a][b]==crt:
                        new_work.append((a, b))
                        visited[a][b]=True
                work = new_work
print(cnt_b)
