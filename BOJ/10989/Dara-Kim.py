import sys

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(sys.stdin.readline())] += 1

for num in range(10001):
    if count[num] != 0:
        for _ in range(count[num]):
            print(num)
