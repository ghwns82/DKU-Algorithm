# 1629

def cal(a, b, c):
    if b <=1:
        return a %c
    elif b % 2 :
        return (((cal(a, b//2, c) **2)%c) *a)%c
    else:
        return (cal(a, b//2, c) **2)%c

a,b,c = map(int, input().split())
print(cal(a,b,c))
