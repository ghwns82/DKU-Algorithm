# 2407
memo=[[0]*101 for _ in range(101)]
n, r = map(int, input().split())
def cal(n,r):
    if n < r*2:
        r = n-r
    if n==r or r==0:
        memo[n][r]=1
        return 1
    if memo[n][r]:
        return memo[n][r]
    else:
        memo[n][r] = cal(n-1, r) + cal(n-1, r-1)
        return memo[n][r]
print(cal(n,r))
