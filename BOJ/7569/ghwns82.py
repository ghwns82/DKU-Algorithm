#  7569
m,n,h = map(int, input().split())
tomatos = [[ input().split() for _ in range(n)] for __ in range(h)]
work = []
for i, box in enumerate(tomatos):
    for j, line in enumerate(box):
        for k, tomato in enumerate(line):
            if tomato =='1':
                work.append((i,j,k))
day=-1
while work:
    crt_work = work
    work=[]
    
    for crt in crt_work:
        x,y,z=crt
        if x>=1 and tomatos[x-1][y][z]=='0':
            tomatos[x-1][y][z]='1'
            work.append((x-1,y,z))
        if y>=1 and tomatos[x][y-1][z]=='0':
            tomatos[x][y-1][z]='1'
            work.append((x,y-1,z))
        if z>=1 and tomatos[x][y][z-1]=='0':
            tomatos[x][y][z-1]='1'
            work.append((x,y,z-1))
            
        if x<h-1 and tomatos[x+1][y][z]=='0':
            tomatos[x+1][y][z]='1'
            work.append((x+1,y,z))
        if y<n-1 and tomatos[x][y+1][z]=='0':
            tomatos[x][y+1][z]='1'
            work.append((x,y+1,z))
        if z<m-1 and tomatos[x][y][z+1]=='0':
            tomatos[x][y][z+1]='1'
            work.append((x,y,z+1))
    day +=1
Flag = False
for i, box in enumerate(tomatos):
    for j, line in enumerate(box):
        for k, tomato in enumerate(line):
            if tomato =='0':
                print(-1)
                Flag = True
                break
        if Flag:
            break
    if Flag:
        break
else:
    print(day)

