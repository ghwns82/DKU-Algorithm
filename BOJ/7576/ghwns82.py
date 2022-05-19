import sys
input = sys.stdin.readline

m,n = map(int, input().split())
tomatos = [ input().split() for _ in range(n)]
work = []
for i, line in enumerate(tomatos):
    for j, tomato in enumerate(line):
        if tomato =='1':
            work.append((i,j))
day=-1
while work:
    crt_work = work
    work=[]
    for crt in crt_work:
        x,y=crt
        if x>=1 and tomatos[x-1][y]=='0':
            tomatos[x-1][y]='1'
            work.append((x-1,y))
        if y>=1 and tomatos[x][y-1]=='0':
            tomatos[x][y-1]='1'
            work.append((x,y-1))
        if x<n-1 and tomatos[x+1][y]=='0':
            tomatos[x+1][y]='1'
            work.append((x+1,y))
        if y<m-1 and tomatos[x][y+1]=='0':
            tomatos[x][y+1]='1'
            work.append((x,y+1))
    day +=1
for i, line in enumerate(tomatos):
    for j, tomato in enumerate(line):
        if tomato =='0':
            print(-1)
            break
    if tomato == '0':
        break
else:
    print(day)
