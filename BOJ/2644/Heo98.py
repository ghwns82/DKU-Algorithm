import sys

input=sys.stdin.readline

'''
첫재 줄 N 총 사람 수 
촌수 계산 할 사람 번호 두개
관계의 개수 m
부모 자식간의 관계 x y x는 자식 y는 부모
'''

import sys
sys.setrecursionlimit(100000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
n = int(input())

graph = [[] for _ in range(n+1)]

s, e = map(int, input().split())

for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

check = [0]*(n+1)

dfs(s)
print(check[e] if check[e] > 0 else -1)
