import sys

T = int(input())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for m in range(M):
        a, b = map(int, sys.stdin.readline().split())

    print(N-1)
