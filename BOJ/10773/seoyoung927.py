N=int(input())
llist=[]
for _ in range(0,N):
    num=int(input())
    #0이 나오면 스택에서 삭제한다.
    if(num==0):
        llist.pop()
    #그렇지 않으면 스택에 삽입한다.
    else:
        llist.append(num)
print(sum(llist))
