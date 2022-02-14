result = 1
for n in range(3):
    result *= int(input())
dic = {}
for n in str(result):
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

for i in range(10):
    if str(i) not in dic.keys():
        print(0)
    else:
        print(dic[str(i)])