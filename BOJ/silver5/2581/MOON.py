start_num = int(input())
last_num = int(input())

slist = []
for num in range(start_num, last_num + 1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            slist.append(num)

if len(slist) > 0:
    print(sum(slist))
    print(min(slist))
else:
    print(-1)
