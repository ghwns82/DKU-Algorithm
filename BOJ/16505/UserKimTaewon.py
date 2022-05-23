from itertools import pairwise
def nextstar(x):
    yield '*'
    for i in pairwise(x):
        if i.count('*')==1:
            yield '*'
        else:
            yield ' '
    yield '*'
def main():
    n=int(input())
    n=2**n
    buf=[]
    x='*'
    for _ in range(n):
        buf.append(x)
        x=''.join(nextstar(x))
    for i in reversed(buf):
        print(i)
if __name__=='__main__':
    main()
