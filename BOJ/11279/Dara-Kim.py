import sys
import heapq

N = int(input())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            print('0')
        else:
            print((-1)*heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1)*x)
