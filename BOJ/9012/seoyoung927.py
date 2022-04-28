#괄호 실버4
import sys

N=int(sys.stdin.readline())
#N=6

def is_parenthesis_string(arr):
    llist=[]
    
    for item in arr:
        if(item=='('):
            llist.append('(')
        elif(item==')'):
            if(len(llist)==0):
                return False
            else:
                a=llist.pop()
    
    if(len(llist)==0):
        return True
    else:
        return False

for i in range(N):
    arr=sys.stdin.readline()
    #arr=input()
    if(is_parenthesis_string(arr)):
        print("YES")
    else:
        print("NO")
