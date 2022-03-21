'''
    K번째 사람을 제거한 후 제겋나 사람의 바로 다음 순서에 존재하는 
    사람을 기준으로 K번째 사람을 죽이는 것
'''

import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int, input().split())
queue=deque()
prt_list_=[]
chk=0

for i in range(1, N+1):
    queue.append(i)

while queue:
    queue.rotate(-(K-1))
    a = queue.popleft()
    prt_list_.append(a)
        
print("<",end="")
for i in range(len(prt_list_)):
    if i ==(len(prt_list_)-1):
        print(prt_list_[i],end="")
    else:
        print(prt_list_[i],end=", ")
print(">")







