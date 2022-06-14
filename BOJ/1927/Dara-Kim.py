import sys, heapq

N = int(input())
heap = []

for n in range(N):
    x = int(sys.stdin.readline())
    if not x:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
