import sys
input=sys.stdin.readline
num=int(input())
answer=[]
for i in range(num):
    N,M=map(int,input().split())
    queue_list=list(map(int,input().split()))
    chk=[False]*N
    chk[M]=True
    bool=True
    count=1
    while(bool):
        max_index=queue_list.index(max(queue_list))
        if chk[max_index]==True:
            answer.append(count)
            bool=False
        else:
            queue_list=queue_list[max_index+1:]+queue_list[:max_index]
            chk=chk[max_index+1:]+chk[:max_index]
            count+=1

print("\n".join(str(i) for i in answer))
