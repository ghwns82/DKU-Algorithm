from collections import deque
import sys

input= sys.stdin.readline

N=int(input())

deque_=[]
print_=[]

for i in range(N):
    s=input().strip()
    if 'push_back' in s:
        deque_.append(s[10:])
    elif 'push_front' in s:
        deque_=[s[11:]]+deque_
    elif s=='pop_front':
        if len(deque_)>0:
            print_.append(deque_[0])
            deque_=deque_[1:]
        else:
            print_.append(-1)
    elif s=='pop_back':
        if len(deque_)>0:
            print_.append(deque_[-1])
            deque_=deque_[:-1]
        else:
            print_.append(-1)
    elif s=='size':
        print_.append(len(deque_))
    elif s=='empty':
        if len(deque_)>0:
            print_.append(0)
        else:
            print_.append(1)
    elif s=="front":
        if len(deque_)>0:
            print_.append(deque_[0])
        else:
            print_.append(-1)
    elif s=='back':
        if len(deque_)>0:
            print_.append(deque_[-1])
        else:
            print_.append(-1)

for i in print_:
    print(i)
