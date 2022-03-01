# 11047
n,k=map(int, input().split())
coins=[int(input()) for _ in range(n)]
money = k
cnt=0
for coin in coins[::-1]:
    if money//coin:
        cnt += money//coin
        money%=coin
print(cnt)
