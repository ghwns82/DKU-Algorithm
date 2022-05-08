import sys
from collections import deque

def push(X):
    Queue.append(X)

def pop():
    if not Queue:
        print("-1")
    else:
        print(Queue.popleft())

def size():
    print(len(Queue))

def empty():
    if not Queue:
        print(1)
    else:
        print(0)

def front():
    if not Queue:
        print("-1")
    else:
        print(Queue[0])

def back():
    if not Queue:
        print("-1")
    else:
        print(Queue[-1])

Queue = deque()
N = int(input())

for a in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'front':
        front()
    else:
        back()
