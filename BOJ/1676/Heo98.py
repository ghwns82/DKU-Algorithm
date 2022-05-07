import sys

input=sys.stdin.readline

N=int(input())
count_2=0
count_5=0
for i in range(1,N+1):
    while(1):
        if(i%2==0):
            count_2+=1
            i/=2
        elif(i%5==0):
            count_5+=1
            i/=5
        else:
            break


print(min(count_2,count_5))

