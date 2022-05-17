import sys
import math

N = int(input())
radiusList = list(map(int, sys.stdin.readline().split()))

radius0 = radiusList[0]

for rad in range(1, len(radiusList)):
    gcd = math.gcd(radius0, radiusList[rad])
    print(f'{radius0//gcd}/{radiusList[rad]//gcd}')
