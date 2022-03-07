# 2630
import sys
input = sys.stdin.readline

N= int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result=[0,0]
def cut(n, part):
    re = sum(sum(part,[]))
    if re ==n*n:
        result[1]+=1
        return 0
    if re==0:
        result[0]+=1
        return 0
    n = n//2
    cut(n, [i[:n] for i in part[:n]])
    cut(n, [i[n:] for i in part[:n]])
    cut(n, [i[:n] for i in part[n:]])
    cut(n, [i[n:] for i in part[n:]])

cut(N, paper)
print(*result, sep='\n')
