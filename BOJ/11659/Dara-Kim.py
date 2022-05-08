import sys

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))

sumList = [0]
sum = 0
for i in range(len(numList)):
    sum += numList[i]
    sumList.append(sum)

for b in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sumList[j] - sumList[i - 1])
