# 9375
for _ in range(int(input())):
    clothes={}
    for __ in range(int(input())):
        value, key = input().split()
        if key in clothes.keys():
            clothes[key].append(value)
        else:
            clothes[key]=[value]
    result=1
    for i in clothes.values():
        result*=len(i)+1
    print(result-1)
