# 11727
n = int(input())
result = [0]*(n+2)
result[1] = 1
result[2] = 3
if n<3:
    print(result[n])
else:
    for i,v in enumerate(range(n-2),3):
        result[i] = result[i-2]*2 + result[i-1]
    print(result[n]%10007)
