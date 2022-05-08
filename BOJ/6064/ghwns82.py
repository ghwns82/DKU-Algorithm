import sys
input = sys.stdin.readline
# 6064
for _ in range(int(input())):
    n,m,x,y=map(int, input().split())
    if n>m:
        n,m,x,y = m,n,y,x
    while y< m*n :
        if y % n == x%n:
            break
        y+=m
    else:
        y=-1
    print(y)
