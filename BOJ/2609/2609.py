import sys
import math

# 유클리드 호제법

# gcd(a,b)
# a와 b의 최대공약수 = (a%b)와 b의 최대공약수
# g(n,0) = 0

# lcm(a,b)
# a와 b는 g(a와 b의 최대공약수)에 최대공약수가 1인 a'와 b'가 곱해진 수
# a = a'*g / b = b'*g / gcd(a,b) = 1

m, n = map(int, sys.stdin.readline().split())
print(math.gcd(m,n))
print(math.lcm(m,n))