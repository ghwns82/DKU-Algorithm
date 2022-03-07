from math import gcd
input()
rings = list(map(int, input().split()))
recent=rings[0]
for i,v in enumerate(rings[1:],1):
    g=gcd(recent,v)
    print(f'{recent//g}/{v//g}')
