N = int(input())
V = [input().split() for _ in range(6)]
DList = [int(v[0]) for v in V]
LList = [int(v[1]) for v in V]
BigBox, SmallBox = 1, 1

for a in range(1, 5):
    if DList.count(a) == 1:
        idx = DList.index(a)
        BigBox *= LList[idx]
        if idx >= 3:
            idx -= 6
        SmallBox *= LList[idx + 3]
        
Field = BigBox - SmallBox
print(Field * N)
