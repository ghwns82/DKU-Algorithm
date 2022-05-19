import sys

input=sys.stdin.readline


'''
1 -> 1
2 -> 11, 2
3 -> 111 , 12, 21, 3
4 -> 13, 112, 22, 1111, 121, 211, 31

이 4개만 보면 
1번째 단계 숫자에 4를 만들 수 있는 특정값을 더해줌 1 3
2번째 단계에서도 똑같이 4를 만들 수 있는 특정값을 더해줌 112, 22
3번째 단계 1111, 121, 211, 31 이런식 무조건 하나씩만 더해지기 때문에
r[i]=r[i-3]+r[i-2]+r[i-1]
이라는 점화식이 나옴. 
'''

T=int(input().strip())

list_=[0,1,2,4]+[0]*8
for _ in range(T):
    n=int(input().strip())
    for k in range(4,n+1):
        list_[k]=list_[k-3]+list_[k-2]+list_[k-1]
    print(list_[n])



