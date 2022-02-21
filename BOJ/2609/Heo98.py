# 소수를 구한뒤 나누기를 하여 최대공약수 최소공배수를 구하기에는 시간제한때문에 힘듦.
# 물론 추측이지만 for문이 많이 사용되어 그런 생각을 함. 
# 유클리드 공식을 사용하면 b,0의 최대공약수는 자기 자신이라는 성질을 사용함. 
# 그리고 a,b 의 최대 공약수는 a, b%a 와 같다는 것을 알아야함. 

import sys

input=sys.stdin.readline

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a,b=map(int, input().split())
gcd_num=gcd(a,b)
prime_a=a//gcd_num
prime_b=b//gcd_num
print(gcd_num)
print(gcd_num*prime_a*prime_b)
