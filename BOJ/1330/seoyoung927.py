import sys

N1, N2 = map(int, sys.stdin.readline().split())

if(N1<N2):
    print('<')
elif(N1>N2):
    print('>')
else:
    print("==")
