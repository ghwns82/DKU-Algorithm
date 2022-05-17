import sys

input=sys.stdin.readline

express_= input().split('-')
li=[]
for i in range(len(express_)):
    li.append(sum(map(int,express_[i].split('+'))))

result=li[0]
for i in range(1,len(li)):
    result-=li[i]
print(result)
