import sys

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

C = int(input())
N = int(input())
dic = {}

for c in range(C):
    dic[c+1] = set()

for n in range(N):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

visited = []
bfs(1, dic)
print(len(visited)-1)
