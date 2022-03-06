import sys

input=sys.stdin.readline
N=int(input())
queue_=[]
print_=[]

for i in range(N):
    s=input().strip()
    if s=="front":
        if len(queue_)==0:
            print_.append(-1)
        else:
            print_.append(queue_[0])
    elif s=="back":
        if len(queue_)==0:
            print_.append(-1)
        else:
            print_.append(queue_[-1])
    elif s=="empty":
        if len(queue_)==0:
             print_.append(1)
        else:
             print_.append(0)
    elif s=="size":
        print_.append(len(queue_))
    elif s=="pop":
        if len(queue_)==0:
             print_.append(-1)
        else:
            print_.append(queue_[0])
            del queue_[0]
    elif 'push' in s:
        k=int(s[5:])
        queue_.append(k)

for i in print_:
    print(i)
