import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
Ms = list(map(int, sys.stdin.readline().split()))

A = sorted(A)

def binarySearching(a):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == a:
            return 1
        elif A[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for a in Ms:
    if binarySearching(a) == 0:
        print("0")
    else:
        print("1")
