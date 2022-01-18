import sys

cnt = int(sys.stdin.readline())
for j in range(cnt):
    n, ch = sys.stdin.readline().split()
    answer = ""
    n = int(n)
    for c in ch:
        answer += c*n
    print(answer)