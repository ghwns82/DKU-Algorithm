import sys

def push(X):
    Stack.append(X)

def pop():
    if not Stack:
        print(-1)
    else:
        print(Stack.pop())

def size():
    print(len(Stack))

def empty():
    if not Stack:
        print(1)
    else:
        print(0)

def top():
    if not Stack:
        print(-1)
    else:
        print(Stack[-1])

N = int(input())
Stack = []

for a in range(N):
    order = sys.stdin.readline().split()
    order0 = order[0]
    if order0 == 'push':
        push(order[1])
    elif order0 == 'pop':
        pop()
    elif order0 == 'size':
        size()
    elif order0 == 'empty':
        empty()
    else:
        top()
