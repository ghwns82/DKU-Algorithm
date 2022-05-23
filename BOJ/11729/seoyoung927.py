import sys

N=int(sys.stdin.readline())
cnt=0
result=[]

def hanoi(n, src, tmp, des):
    global cnt
    cnt=cnt+1
    if(n>1):
        hanoi(n-1, src, des, tmp)
        result.append((src, des))
        hanoi(n-1, tmp, src, des)
    else:#n==1
        result.append((src, des))

    
hanoi(N, 1,2,3)
print(cnt)
for item in result:
    print(item[0], item[1])
