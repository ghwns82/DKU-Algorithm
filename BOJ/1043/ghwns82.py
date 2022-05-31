n, m = map(int, input().split())
true = set(map(int, input().split()[1:]))
parties = [set(map(int, input().split()[1:])) for _ in range(m)]

num_true = 0
lie_party = [1]*m
while 1:
    if num_true != len(true):
        num_true = len(true)
    else:
        break
    for i in true:
        for j, party in enumerate(parties):
            if i in party:
                true=true|party
                lie_party[j]=0
                
print(sum(lie_party))            
