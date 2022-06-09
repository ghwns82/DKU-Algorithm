# 14425

n,m = map(int, input().split())

words=set(input() for i in range(n))

print(sum([True for i in range(m) if input() in words]))
