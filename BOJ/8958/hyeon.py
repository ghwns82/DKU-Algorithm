import sys

cnt = int(sys.stdin.readline())
for i in range(cnt):
    check = sys.stdin.readline().rstrip()
    pre = 1
    result = 0
    for c in check:
        if c == 'X':
            pre = 1
        else:
            result += pre
            pre += 1
    print(result)