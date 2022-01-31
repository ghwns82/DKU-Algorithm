import sys
input=sys.stdin.readline


N=int(input())
input_list=[int(input()) for _ in range(N)]
num=1
result=[]
stack=[]
for i in range(len(input_list)):
    while input_list[i]>=num:
        stack.append(num)
        result.append("+")
        num+=1

    if input_list[i]==stack[-1]:
        result.append('-')
        stack.pop()    
    
    if i==len(input_list)-1:
        if len(stack)!=0:
            print("NO")

        else:
            for k in range(len(result)):
                print(result[k])
