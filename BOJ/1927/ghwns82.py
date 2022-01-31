import sys
input = sys.stdin.readline
import heapq
heap=[]
for _ in range(int(input())):
    if (x:=int(input())) == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
        
