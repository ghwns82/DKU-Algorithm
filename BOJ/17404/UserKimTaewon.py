n=int(input())
house=tuple(tuple(map(int,input().split())) for _ in range(n))
choice=frozenset(range(3))

from functools import cache
from sys import setrecursionlimit

setrecursionlimit(10**5)

def skip(i,n):
    yield from range(i)
    yield from range(i+1,n)

@cache
def mincost(th,prev,first):
    if th==n-1:
        return min(house[th][i] for i in (choice-{prev,first}))
    return min(house[th][i]+mincost(th+1,i,first)for i in skip(prev,3))
print(min(house[0][i]+mincost(1,i,i)for i in range(3)))
