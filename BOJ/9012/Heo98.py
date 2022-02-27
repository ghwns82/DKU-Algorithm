import sys

input=sys.stdin.readline

N=int(input())
ans=[]
for i in range(N):
    chk=True
    stack=[]
    str_=input()
    for k in str_:
        if k=='(':
            stack.append("(")
        elif k ==")" :
            if stack == []:
                chk=False
                break
            elif stack[-1]=="(":
                stack.pop()
    if stack != []:
        chk=False
    if chk==True:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)
