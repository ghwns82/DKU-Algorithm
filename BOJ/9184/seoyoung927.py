import sys

arr=[]
for i in range(22):
    arr.append([])
    for j in range(22):
        arr[i].append([])
        for k in range(22):
            arr[i][j].append(0)

for _a in range(0,21,1):
    for _b in range(0,21,1):
        for _c in range(0,21,1):
            if(_a==0 or _b==0 or _c==0):
                arr[_a][_b][_c]=1
            if(_a<_b and _b<_c+1):
                arr[_a][_b][_c+1]+=arr[_a][_b][_c]
            if(_a<_b+1 and _b+1<_c+1):
                arr[_a][_b+1][_c+1]+=arr[_a][_b][_c]
            if(_a<_b+1 and _b+1<_c):
                arr[_a][_b+1][_c]-=arr[_a][_b][_c]
            if(not(_a+1<_b and _b<_c)):
                arr[_a+1][_b][_c]+=arr[_a][_b][_c]
            if(not(_a+1<_b+1 and _b+1<_c)):
                arr[_a+1][_b+1][_c]+=arr[_a][_b][_c]
            if(not(_a+1<_b and _b<_c+1)):
                arr[_a+1][_b][_c+1]+=arr[_a][_b][_c]
            if(not(_a+1<_b+1 and _b+1<_c+1)):
                arr[_a+1][_b+1][_c+1]-=arr[_a][_b][_c]              

answer=[]
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if(a==-1 and b==-1 and c==-1):
        break
    
    if(a<=0 or b<=0 or c<=0):
        answer.append([a,b,c,1])
    elif(a>20 or b>20 or c>20):
        answer.append([a,b,c,arr[20][20][20]])
    else:
        answer.append([a,b,c,arr[a][b][c]])

for a in answer:
    print('w({}, {}, {}) = {}'.format(a[0],a[1],a[2],a[3]))
