import sys

N=int(sys.stdin.readline())
S=[sys.stdin.readline().split() for _ in range(N)]
S_age = sorted(set([int(s[0]) for s in S]))
dd = {}

for i in S:
    age,name = int(i[0]),i[1]
    if age in dd:
        dd[age].append(name)
    else:
        dd[age]=[name]

for age in S_age:
    for name in dd[age]:
        print(age, name)
