import sys
cnt = int(sys.stdin.readline())
data = []
d = {}
max_cnt = 1
for i in range(cnt):
    value = int(sys.stdin.readline())
    data.append(value)
    if value not in d.keys():
        d[value] = 1
    else:
        d[value] += 1
        if max_cnt < d[value]:
            max_cnt = d[value]
data.sort()
print(round(sum(data)/cnt))
print(data[len(data)//2])

answer3 = []
for key, value in d.items():
    if value == max_cnt:
        answer3.append(key)
answer3.sort()
if len(answer3) > 1:
    print(answer3[1])
else:
    print(answer3[0])
print(max(data)-min(data))