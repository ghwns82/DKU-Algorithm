import sys

N=int(sys.stdin.readline())
arr=[i for i in range(1,N+1)]

idx=0
for _ in range(N-1):
    #제일 위에 있는 카드를 버린다.
    idx+=1
    #두번 째 카드를 가장 밑으로 보낸다.
    arr.append(arr[idx])
    idx+=1

print(arr[idx])
