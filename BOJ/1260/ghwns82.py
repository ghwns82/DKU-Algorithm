n,m,v = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for i in range(n+1) ]
for a,b in lines:
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

def dfs(v):
    work =[v]
    
    while work:
        dot = work.pop(0)
        if visited[dot]==0:
            work = graph[dot] + work
            print(dot, end=' ')
            visited[dot]=1
    print()
def bfs(v):
    work =[v]
    
    while work:
        dot = work.pop(0)
        if visited[dot]==0:
            work = work + graph[dot]
            print(dot, end=' ')
            visited[dot]=1
    print()
visited = [0]*(n+1)
dfs(v)
visited = [0]*(n+1)
bfs(v)
