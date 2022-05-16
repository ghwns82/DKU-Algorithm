# 16953
a, b = map(int, input().split())
work = [a]
cnt=1
end = False

while work:
    cnt+=1
    new_work = []
    for i in work:
        for x in [2*i, int(str(i)+"1")]:
            if x == b:
                print(cnt)
                end = True
                break
            elif x < b:
                new_work.append(x)
        if end:
            break
    if end:
        break
    work = new_work
else:
    print(-1)
