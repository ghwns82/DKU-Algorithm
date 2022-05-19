import sys

N = int(sys.stdin.readline())
numList = [int(sys.stdin.readline().strip()) for _ in range(N)]

for a in sorted(numList):
    print(a)
