# 11726
n = int(input())
a, b = 1,2
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    for i,v in enumerate(range(n-2),3):
        a,b = b, a+b
    print(b%10007)
