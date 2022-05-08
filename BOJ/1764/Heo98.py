import sys

input=sys.stdin.readline

N, M = map(int,input().split())

no_listen=set(input().strip() for _ in range(N))
no_see=set(input().strip() for _ in range(M))

no_listen_see=list(no_listen&no_see)
no_listen_see.sort()
print(len(no_listen_see))
print("\n".join(str(x) for x in no_listen_see))

