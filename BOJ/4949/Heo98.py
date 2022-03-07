import sys

while True:
    check=True
    stack=[]
    line=sys.stdin.readline().rstrip()
    if line=='.':
        break
    for i in line:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack==[] or stack[-1]=='[':
                check=False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif i==']':
            if stack==[] or stack[-1]=='(':
                check=False
                break
            elif stack[-1]=='[':
                stack.pop()
    if stack!=[] or check==False:
        print('no')
    else:
        print('yes')
