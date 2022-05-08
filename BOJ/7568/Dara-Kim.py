N = int(input())

personList = []
for a in range(N):
    w, h = map(int, input().split())
    personList.append((w, h))


for b in personList:
    rank = 1
    for c in personList:
        if (b[0] < c[0] and b[1] < c[1]):
            rank += 1
    print(rank, end = " ")
