# 10815
# 1
int(input())
cards=set(map(int, input().split()))
int(input())
for i in list(map(int, input().split())):
    if i in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
