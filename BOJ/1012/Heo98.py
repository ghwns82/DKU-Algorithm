"""
'''
가장 먼저 배추밭을 만들어야 할 것 이다. 
그 뒤에 배추가 모여있는 집합을 찾아야한다. 떨어져있으면 거기서 끝이다. 
방문하면 방문했다고 chk를 해준다. 집합을 한 개씩 쌓이면 

count를 증가시켜준다. 
하나씩 확인할 필요없이 그냥 받은 입력을 바로 list에 저장해서 그곳으로 가서 확인하면 될 듯 
count 먼저 하고 그 점에서 탐색을 함 list안에 있는 점에서 그리고 하나씩 없애면 될 듯.  상하좌우 확인하는게 좋을 듯 재귀문 써야할듯
'''
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find_area(find_num):
    arr_.remove(find_num)
    # 우측
    if [find_num[0]+1,find_num[1]] in arr_:
        find_area([find_num[0]+1,find_num[1]])
    # 좌측
    elif [find_num[0]-1,find_num[1]] in arr_:
        find_area([find_num[0]-1,find_num[1]])
    # 위
    elif [find_num[0],find_num[1]+1] in arr_:
        find_area([find_num[0],find_num[1]+1])
    # 아래
    elif [find_num[0],find_num[1]-1] in arr_:
        find_area([find_num[0],find_num[1]-1])

T=int(input().rstrip())
for i in range(T):
    M,N,K = map(int, input().rstrip().split())
    arr_=[]
    count=0
    for num_ in range(K):
        row_,col_=map(int, input().rstrip().split())
        arr_.append([row_,col_])
    while(len(arr_)!=0):
        find_num=arr_[0]
        find_area(find_num)
        count+=1
    print(count)
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

def find_(x,y):
    
    if x>=n or x<0 or y>=m or y<0:
      return False
    if lst[x][y] == 1:
      lst[x][y] = 0
  
      find_(x-1,y)
      find_(x+1,y)
      find_(x,y-1)
      find_(x,y+1)
  
      return True
    return False
  
for _ in range(T):
  result = 0
  m,n,baechu = map(int,input().split())
  #리스트에 맵 생성
  lst = [[0 for _ in range(m)] for i in range(n)]
  
  for _ in range(baechu):
    y,x = map(int,input().split())
    lst[x][y] = 1
  
  for i in range(n):
    for j in range(m):
      if find_(i,j) == True:
        result+=1

  print(result)
