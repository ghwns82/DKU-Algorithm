# 실패한 풀이 + 성공한 
"""
'''
먼저 번호 N을 받는다
고장난 번호를 받는다. 
시작 번호는 100이다. 

100에서 그냥 +- 버튼을 누르는게 이득인 경우
일단 list_의 길이가 3보다 작거나 같은 경우를 확인해보면 될 듯
여기서 두가지 체크 그냥 +-를 할 것인가 아니면 번호를 칠 것 인가.
번호를 치는 경우는 다 쳐야함.  
아닌 경우
1. 번호를 하나씩 치고 +-를 하는 경우. 
2  번호가 다른 것중 자리수가 가장 높은거 체크해서 +- 한 경우나 아니면 다음으로 큰 자리수에서 +-를 한다.

가장 가깝게 어떻게 만들수 있을까?



+-만 누르는 경우
숫자를 입력하고 +-를 입력하는 경우 
숫자를 입력하되 가장 가까운 수를 찾기 제일 큰 인덱스에서 찾는거지 broken안된걸로 만들수 있는. 
'''
import sys

input=sys.stdin.readline

N=input().rstrip()
M=int(input().rstrip())

# 고장난 번호
if M!=0:
    broken_=list(map(int,input().rstrip().split(" ")))
else:
    broken_=[]

# 이루어진 수 
list_=[int(x) for x in N]

# 시작점
start_=[1,0,0]



count_1=0
count_2=0
count_3=0
if len(list_)<=3:
    if start_==list_:
        print(0)
    else:
        for index_,num in enumerate(list_):
            chk=num
            chk_count=0
            # 3자리 수 이하일 때 번호를 치는 형식
            if num not in broken_:
                count_1+=1
            else:
                while(chk not in broken_):
                    chk+=1
                    chk_count+=1
                chk=num
                while(chk not in broken_):
                    chk-=1
                    chk_count-=1
                if chk_count<0:
                    count_1+= (num-chk)*pow(10,len(list_)-index_-1)
                else:
                    count_1+= (chk-num)*pow(10,len(list_)-index_-1)
        
        for index_,num in enumerate(list_):
            if num not in broken_:
                count_2+=1
            else:
                
            # 번호를 치지 않고 +,- 만하는 경우
        chk=100

"""

# 간단하게 생각해보자

import sys
input=sys.stdin.readline

target=int(input())
broken_num=int(input())
if broken_num:
    broken_button=list(map(int, input().split()))
else:
    broken_button=[]
# 현재 채널 100번에서 진짜 + -로만 움직이는 경우
min_num=abs(100-target)

# 자 이제 500,000번까지 채녈이 있다. 
# 노가다를 할거다 하나씩 확인하는 과정을 수행할 예정.
# 수빈이가 찾을 채널의 범위가 500,000이라고 했지 우리가 찾을 채널의 범위가 500,000  
# 이 아니다. 그래서 500,000 을 찾을 때 500,001이 500,000으로 갈 수 있는 가장 작은 수가 될 수 있다.

for num in range(1000001):
    num=str(num)
    for digit in range(len(num)):
        if int(num[digit]) in broken_button:
            break
        # 한개도 부서진 번호가 없다.
        elif digit== len(num)-1:
            min_num=min(min_num, abs(target-int(num))+len(num))   

print(min_num)
