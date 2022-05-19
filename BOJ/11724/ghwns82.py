# 11724
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph=[[]for i in range(n+1)]
visit_list=[False]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(1, n+1):
    if not visit_list[i]:
        visit_list[i]=1
        cnt+=1
        work = [*graph[i]]
        while work:
            dot = work.pop()
            if not visit_list[dot]:
                visit_list[dot]=True
                work += [*graph[dot]]
                
print(cnt)
