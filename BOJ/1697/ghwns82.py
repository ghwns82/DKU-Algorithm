from collections import deque

n, k = map(int, input().split())

visted = [0]*100_001
sujin = deque([n])
visted[n]=1
while 1:
    x = sujin.popleft()
    for i in [x-1, x+1, 2*x]:
        if 0<=i<=100_000 and visted[i]==0:
            sujin.append(i)
            visted[i] = visted[x]+1
        if i==k:
            break
    if i==k:
        break
print(visted[i]-1)
