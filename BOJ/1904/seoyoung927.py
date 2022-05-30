import sys

N=int(sys.stdin.readline())

B=[0 for i in range(1000001)]
B[0]=0
B[1]=1
B[2]=2
for i in range(3,N+1):
    B[i]=(B[i-1]+B[i-2])%15746

print(B[N])
