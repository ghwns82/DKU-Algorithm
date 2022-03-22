# 2606

n=int(input())
network = [list(map(int, input().split())) for _ in range(int(input()))]
computers = [0]*(n+1)
computers[1]=1
work=set([1])
while work:
    virus = work.pop()
    for i in network:
        if virus in i:
            work.add(i[0])
            work.add(i[1])
            computers[i[0]]=1
            computers[i[1]]=1
            network.remove(i)
print(sum(computers)-1)
