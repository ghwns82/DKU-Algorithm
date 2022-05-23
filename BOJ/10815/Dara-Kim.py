import sys

N = int(input())
Ns = set(map(int, sys.stdin.readline().split()))
M = int(input())
Ms = list(map(int, sys.stdin.readline().split()))

for a in Ms:
    if a in Ns:
        print("1", end=" ")
    else:
        print("0", end =" ")
