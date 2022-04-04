import sys

input=sys.stdin.readline

# 사분면으로 생각해보자 .
# 총 4사분면으로 표현을 할 수 있고 총 N-2번 반복해주면 된다. 

N, r, c = map(int, input().split())
cnt = 0

# 왼쪽 위로 생각하고 문제를 풀어야함. 
while(N>1):
    size = (2 ** (N-1))
    if r < size and c < size: # 1사분면
        pass
    elif r < size and c >= size: # 2사분면
        cnt += size ** 2 #오른쪽으로 이동해야함. 2^(n-2) X 2^(n-2) 
        c -= size # c-=size하는 이유는 현재 위치를 다시 초기화해줌. 
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        r -= size 
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)
