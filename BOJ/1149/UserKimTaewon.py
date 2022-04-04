n=int(input())
house=tuple(tuple(map(int,input().split())) for _ in range(n))

from functools import cache
from sys import setrecursionlimit

setrecursionlimit(10**5)

def skip(i,n):
    yield from range(i)
    yield from range(i+1,n)

@cache
def mincost(th,prev):
    if th>=n:
        return 0
    return min(house[th][i]+mincost(th+1,i)for i in skip(prev,3))
print(min(house[0][i]+mincost(1,i)for i in range(3)))
