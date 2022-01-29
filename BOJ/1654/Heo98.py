'''
실패작 1
K,N= map(int, input().split())
K_len=[]

for i in range(K):
    K_len.append(int(input()))
check_list=K_len[:]
div=int((max(K_len)+min(K_len))/2)
print(div)
while(True):
    sum=0
    for i in K_len:
        sum+=i//div
    if sum==N:
        break
    if len(check_list)<=1:
        if sum<N:
            div-=1
        else:
            div+=1
    else:
        if sum>N:
            check_list.remove(min(check_list))
            div=int((max(check_list)+min(check_list))/2)
        elif sum<N:
            check_list.remove(max(check_list))
            div=int((max(check_list)+min(check_list))/2)
print(div)
타임아웃
'''


'''
실패작 2

K,N= map(int, input().split())
K_list=[]
for i in range(K):
    K_list.append(int(input()))
div=min(K_list)
chk=0
sum=0
while(True):
    pre_div=div
    for i in K_list:
        sum+=int(i//div)
    if sum==N:
        while(True):
            div+=1
            for s in K_list:
                chk+=s//div
            if chk>N:
                div-=1
                print(div)
                break           
    elif sum<N:
        div=int(div/2)
    elif sum>N:
        div=int((div+pre_div)/2)
print(div)
'''

K,N= map(int, input().split())
Lan_list=[]
for i in range(K):
    Lan_list.append(int(input()))
start,end= 1,max(Lan_list)

while start <= end:
    mid =(start+end)//2
    lines=0
    for i in Lan_list:
        lines+=i//mid
    if lines>=N: # 분기점을 바꿔줌
        start=mid+1
    else:
        end=mid-1
print(end)
