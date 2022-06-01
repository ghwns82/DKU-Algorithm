N, M = map(int, input().split())
j = int(input())
apple = []
move = 0

for _ in range(j):
    apple.append(int(input()))

move = 0
end = M
start = 1

for i in range(j):
    if (end >= apple[i] and start <= apple[i]):
        continue
    elif (end < apple[i]):
        move += apple[i] - end
        end = apple[i]
        start = apple[i] - (M - 1)
    elif (start > apple[i]):
        move += start - apple[i]
        start = apple[i]
        end = apple[i] + (M - 1)

print(move)
