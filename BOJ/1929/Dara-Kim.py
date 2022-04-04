import sys

M, N = map(int, input().split())

numList = [True for i in range(N + 1)]
numList[0] = False
numList[1] = False

sqrtN = int(N ** 0.5)
for a in range(sqrtN + 1):
    if numList[a]:
        for b in range(a * 2, N + 1, a):
            numList[b] = False

for c in range(M, len(numList)):
    if numList[c]:
        print(c)
