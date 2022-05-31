import sys

N=int(sys.stdin.readline())
S=list(set([sys.stdin.readline().split()[0] for _ in range(N)]))
S=sorted(S, key=lambda x:len(x))
dd=dict()
result=[]

for s in S:
    if len(s) not in dd:
        dd[len(s)]=[s]
    else:
        dd[len(s)].append(s)

for key in dd:
    for val in sorted(dd[key]):
        print(val)
