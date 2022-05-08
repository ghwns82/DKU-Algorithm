def cuttingPaper(x, y, n):
    global wcnt, bcnt
    flag = paper[x][y]

    for a in range(x, x+n):
        for b in range(y, y+n):
            if flag != paper[a][b]:
                cuttingPaper(x, y, n//2)
                cuttingPaper(x, y+n//2, n//2)
                cuttingPaper(x+n//2, y, n//2)
                cuttingPaper(x+n//2, y+n//2, n//2)
                return

    if flag == 0:
        wcnt += 1
    else:
        bcnt += 1
        return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
wcnt, bcnt = 0, 0

cuttingPaper(0, 0, N)
print(wcnt)
print(bcnt)
