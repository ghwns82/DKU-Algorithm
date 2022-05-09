import sys

N1, N2 = map(int, sys.stdin.readline().split())

arr=[0]+list(map(int, sys.stdin.readline().split()))
for i in range(2,N1+1,1):
    arr[i]=arr[i-1]+arr[i]

for i in range(N2):
    tmp1, tmp2 = map(int, sys.stdin.readline().split())
    print(arr[tmp2]-arr[tmp1-1])
