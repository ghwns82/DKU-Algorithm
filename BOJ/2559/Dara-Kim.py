import sys

N, K = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

sum = 0
tempSum = []

for a in range(K):
    sum += temperatures[a]
tempSum.append(sum)

for b in range(N-K):
    sum = tempSum[b]-temperatures[b]+temperatures[b+K]
    tempSum.append(sum)

print(max(tempSum))
