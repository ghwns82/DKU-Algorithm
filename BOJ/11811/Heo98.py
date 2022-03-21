from cmath import inf
import sys
input= sys.stdin.readline
n, m, b = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
height = 0
ans =inf

for i in range(257): # 땅 높이 0~256
    max=0
    min=0
    for j in range(n):
        for k in range(m):
            if table[j][k]<i: # 블럭이 현재 높이보다 작은 경우
                min+=(i-table[j][k]) # 현재 높이가 블록 높이보다 높을 때 (min 만큼 인벤토리에서 꺼내서 채워야함)
            else:
                max+=(table[j][k]-i)
    inven=max+b
    if inven<min: # 못 채우는 경우
        continue
    time=2*max+min
    if time<=ans:
        ans= time
        height=i
print(ans,height)
