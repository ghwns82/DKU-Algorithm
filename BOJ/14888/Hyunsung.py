#14888 연산자 끼워넣기

import sys

def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result

    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if p:
        dfs(cnt + 1, result + s[cnt], p - 1, m, mul, div)

    if m:
        dfs(cnt + 1, result - s[cnt], p, m - 1, mul, div)

    if mul:
        dfs(cnt + 1, result * s[cnt], p, m, mul - 1, div)

    if div:
        if result < 0 :
            dfs(cnt + 1, -(-result // s[cnt]), p, m, mul, div - 1)
        else :
            dfs(cnt + 1, result // s[cnt], p, m, mul, div - 1)

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

max_result = -1000000001
min_result = 1000000001

dfs(1, s[0], op[0], op[1], op[2], op[3])

print(max_result)
print(min_result)