import sys

input=sys.stdin.readline

# 높이가 V이다. 
A,B,V =map(int, input().split())
day_=(V-A)//(A-B)
where_=day_*(A-B)
while(1):
    day_+=1
    where_+=A
    if where_>=V:
        print(day_)
        break
    else:
        where_-=B
