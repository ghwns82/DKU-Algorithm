cnt = int(input())
scores = list(map(int, input().split()))
max = 0
sum = 0
for score in scores:
    if max < score:
        max = score
    sum += score
print(((sum/max)*100)/cnt)