# 11659
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sum_=0
sum_seq= [0]+[sum_:=(sum_+ i) for i in list(map(int, input().split()))]
for _ in range(m):
    start,end = map(int, input().split())
    print(sum_seq[end]-sum_seq[start-1])
