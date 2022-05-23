case = int(input())
for i in range(case):
    count = 0
    a, b = map(int, input().split())
    r = list(range(a, b+1))
    for j in range(len(r)):
        num = str(r[j])
        for k in range(len(num)):
            if num[k] == '0':
                count += 1
    print(count)
