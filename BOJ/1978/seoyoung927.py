import sys

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

def is_sosu(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2, n):
            if(n%i==0):
                return False
    return True

cnt=0
for n in arr:
    if(is_sosu(n)):
        cnt+=1

print(cnt)
