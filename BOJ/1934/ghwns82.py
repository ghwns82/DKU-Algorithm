#1934
for _ in range(int(input())):
    a,b = sorted(list(map(int, input().split())))
    x,y = a,b
    while y%x:
        x,y = y%x, x
    print(a*b//x)
