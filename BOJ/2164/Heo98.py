# N장의 카드가 있고 1~n 까지의 번호 붙어 있고
# 한 장 남을 때까지 반복
# 버리고 그 다음에는 제일 아래로 이동
'''
import sys


input=sys.stdin.readline
N=int(input())
num_list=[i for i in range(1,N+1)]
count=1
while(len(num_list)!=1):
    if count%2==1:
        num_list=num_list[1:]
        count+=1
    else:
        plus_num=num_list[0]
        num_list=num_list[1:]+[plus_num]
        count+=1
print(num_list[0])
for문으로 하면 시간복잡도 때문에 안됨. 
'''
import sys
from collections import deque


input=sys.stdin.readline
N=int(input())
num_list=deque(range(1,N+1))
while(len(num_list)>1):
    num_list.popleft()
    num_list.rotate(-1)
print(num_list[0])
