import sys 
sys.setrecursionlimit(10000)

def dfs(a,b):
    global count
    if a<0 or a>=h or b<0 or b>=w:
        return False
    if (area[a][b]==0):
        area[a][b]=1
        count+=1
        dfs(a+1,b)
        dfs(a-1,b)
        dfs(a,b+1)
        dfs(a,b-1)
        


input= sys.stdin.readline

h,w,k=map(int,input().split())

area=[[0]*(w+1) for _ in range(h+1)]



for _ in range(k):
    a,b,c,d=map(int,input().split())
    for i in range(b,d+1):
        for k in range(a,c+1):
            area[i][k]=1

num=0
area_=[]
for i in range(h+1):
    for k in range(w+1):
        count=0
        dfs(i,k)    
        if count !=0:
            num+=1       
            area_.append(count)

print(num)
         
for a in sorted(area_):
    print(a,end="")
