import sys

N=int(sys.stdin.readline())
S=[int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(S):
    print(i)
