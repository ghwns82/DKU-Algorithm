import sys

N=int(input())

stack_=[]
print_=[]
for i in range(N):
    s=input()
    if s=="top":
        if len(stack_)==0:
            print_.append(-1)
        else:
            print_.append(stack_[-1])
    elif s=="empty":
        if len(stack_)==0:
             print_.append(1)
        else:
             print_.append(0)
    elif s=="size":
        print_.append(len(stack_))
    elif s=="pop":
        if len(stack_)==0:
             print_.append(-1)
        else:
            print_.append(stack_.pop())
    elif "push" in s:
        k=int(s[5:])
        stack_.append(k)

for i in print_:
    print(i)
