import sys

input=sys.stdin.readline

N=int(input())
M=int(input())

com=[]
for i in range(N):
    com.append([])

for i in range(M):
    a,b = input().split()
    com[int(a)-1].append(int(b))

virus=com[0]
for _ in range(N):
    for i in virus:
        for k in com[i-1]:
            if k not in virus:
                virus.append(k)
    
virus=set(virus)
print(len(virus))
