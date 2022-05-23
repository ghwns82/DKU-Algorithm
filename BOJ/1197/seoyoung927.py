import sys

INF = 2147483648
N1, N2 = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(N2):
    v1, v2, val = map(int, sys.stdin.readline().split())
    if val not in graph:
        graph[val] = [(v1, v2)]
    else:
        graph[val].append((v1, v2))

#Kruskal's Algorithm
disjoint_set = []
union_set = [i for i in range(N1+1)]

def initial(N):
    for i in range(1,N+1):
        disjoint_set.append({i})

def find(idx):
    #for sset in disjoint_set:
    #    if idx in sset:
    #        return sset
    if(union_set[idx]==idx):
        return idx
    else:
        return find(union_set[idx])

def merge(set_a, set_b):
    #disjoint_set.remove(set_a)
    #disjoint_set.remove(set_b)
    #disjoint_set(set_a.union(set_b))
    big=max(set_a,set_b)
    small=min(set_a,set_b)
    union_set[big]=small

def kruskal(N, W):
    total=0

    initial(N)
    #이음선을 가중치가 작은 것부터 차례로 정렬
    distance=sorted(W)
    idx=0

    no_edge=0
    while(no_edge < N-1):
        tmp_key=distance[idx]
        if len(W[tmp_key])==0:
            idx+=1
            tmp_key=distance[idx]
        a,b=W[tmp_key].pop() 
        p = find(a)
        q = find(b)
        if(p!=q):
            merge(p, q)
            total+=tmp_key
            no_edge+=1
    
    return total

print(kruskal(N1,graph))
