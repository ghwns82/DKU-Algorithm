#구현을 끝마치고 보니 파이썬의 내장 pow 함수도 mod 인자를 받을 수 있다는 게 떠올랐다. 
"""
MAXP=2
def pow(x,n,m):
    if n<MAXP:
        return (x**m)%m
    if n%2==1:
        return (x*pow(x,n//2,m)**2)%m
    else:
        return (pow(x,n,m)**2)%m
"""

a,b,c=map(int,input().split())
print(pow(a,b,c))
