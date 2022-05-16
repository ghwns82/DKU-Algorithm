import math
memo=input()
dic = dict()
for i,v in enumerate(list(memo),1):
    dic[v] = i
result = 0
unit = len(memo)
for i,v in enumerate(input()[::-1]):
    result += dic[v]* pow(unit, i,900528)
print(result%900528)
