# 11399 ATM
n=int(input())
result=0
people=sorted(list(map(int, input().split())))
for i in people:
    result += n*i
    n-=1
print(result)
