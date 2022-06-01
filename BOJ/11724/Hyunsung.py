#11724 연결 요소의 개수 실버 2

import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start, depth) :
    been[start] = True
    for element in node[start] :
        if not been[element] :
            dfs(element, depth + 1)


N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
been = [False] * (N + 1)
count = 0

for i in range(M) :
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(1, N + 1) :
    if not been[j] :
        if not node[j] :
            count += 1
            been[j] = True
        else:
            dfs(j, 0)
            count += 1

print(count)