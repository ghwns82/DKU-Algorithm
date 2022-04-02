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
