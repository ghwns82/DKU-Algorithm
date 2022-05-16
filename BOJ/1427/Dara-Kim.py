N = int(input())
numList = [i for i in map(int, str(N))]

for i in sorted(numList, reverse=True):
    print(i, end='')
