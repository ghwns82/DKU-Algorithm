# 13305
import sys
input = sys.stdin.readline
input()
kms = list(map(int, input().split()))
cities = list(map(int, input().split()))[:-1]

result=0
cost = cities[0]
for i, city in enumerate(cities):
    if city < cost:
        cost = city
    result+=cost*kms[i]
print(result)
