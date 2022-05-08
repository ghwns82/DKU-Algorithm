import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline())

result=[]
for _ in arr:
    tmp=_.split()
    if tmp[0]=='push':
        result.append(tmp[1])
    elif tmp[0]=='pop':
        if(len(result)==0):
            print(-1)
        else:
            print(result.pop())
    elif tmp[0]=='size':
        print(len(result))
    elif tmp[0]=='empty':
        if(len(result)==0):
            print(1)
        else:
            print(0)
    elif tmp[0]=='top':
        if(len(result)==0):
            print(-1)
        else:
            print(result[-1])
