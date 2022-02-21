# 1966
from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    docs = deque(map(int, input().split()))
    pr =1
    while 1:
        if max(docs)==docs[0]:
            if m ==0:
                print(pr)
                break
            else:
                docs.popleft()
                pr+=1
                m-=1
        else:
            docs.append(docs.popleft())
            if m == 0:
                m= len(docs)-1
            else:
                m-=1
