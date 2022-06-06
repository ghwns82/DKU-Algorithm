import sys

N = int(input())

As = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1] * N

for n in range(N):
    while stack:
        if As[n] > As[stack[-1]]:
            answer[stack.pop()] = As[n]
        else:
            break
    stack.append(n)
print(*answer)
