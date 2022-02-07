n=int(input())
score = [int(input()) for i in range(n)] + [0 for i in range(n,4)]
dp = [score[0], score[0] + score[1], max(score[1] + score[2], score[0]+score[2])]
for i in range(3,n):
    dp.append(max(dp[i-3] + score[i-1]+score[i], dp[i-2] + score[i]))
print(dp[n-1])
