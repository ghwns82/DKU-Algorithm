# 규칙을 아는 경우 쉽게 풀 수 있음
# 아니면 메모이제이션을 통해서도 풀 수 있을듯 귀찮아서 시도는 ㅎㅎ
# 0의 개수는 1의 이전 index의 개수
# 1의 개수는 이전 index의 0의 개수와 다음 index의 0의 개수

import sys

input=sys.stdin.readline



T=int(input())
zero=[1,0]
one=[0,1]

for i in range(T):
    N=int(input())
    if N>=1:
        for k in range(N-1):
            zero.append(one[-1])
            one.append(zero[-2]+zero[-1])
    print(zero[N],one[N])
        


