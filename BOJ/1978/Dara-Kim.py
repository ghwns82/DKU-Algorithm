N = int(input())

numList = list(map(int, input().split()))

count = 0

for a in numList:
    error = 0
    if a > 1:
        for b in range(2, a):
            if a % b == 0:
                error += 1
                break
        if error == 0:
            count += 1

print(count)
