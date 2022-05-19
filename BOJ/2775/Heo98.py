import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())
    list_=[x for x in range(1,n+1)]
    for floor_ in range(k):
        for room_ in range(1,n):
            list_[room_]+=list_[room_-1]
    print(list_[-1])

