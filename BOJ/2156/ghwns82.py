n=int(input())
wines =[int(input()) for _ in range(n)]+[0]*3
dp = [wines[0], wines[0]+ wines[1], max(wines[0],wines[1])+wines[2]] + [0]*n
if n<=3:
    print(max(dp))
else:
    for i in range(3,n+1):
        dp[i] = max(max(dp[:i-1])+wines[i], wines[i]+wines[i-1]+ max(dp[:i-2]))
    print(max(dp))
