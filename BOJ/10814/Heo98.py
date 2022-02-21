'''
# 이와 같이하면 age를 str로 보아 틀림
import sys

input=sys.stdin.readline
N=int(input())

name_list=[input().split() for i in range(N)]
name_list.sort(key= lambda x: x[0])
for i in name_list:
    print(i[0],i[1])

'''



import sys

input=sys.stdin.readline
N=int(input())

name_list=[]
for i in range(N):
    age,name=input().split()
    name_list.append([int(age),name])
name_list.sort(key= lambda x: x[0])
for i in name_list:
    print(i[0],i[1])
