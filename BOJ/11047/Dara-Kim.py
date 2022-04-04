N, K = map(int, input().split())
coinList = [int(input()) for _ in range(N)]

num = 0
for i in reversed(coinList):
    num += K // i
    K %= i

print(num)
