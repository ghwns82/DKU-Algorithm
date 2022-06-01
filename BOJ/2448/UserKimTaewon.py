start=(
'*     ',
'* *   ',
'***** '
)
def gennext(x):
    dum=' '*len(x[0])
    for i in x:
        yield i+dum
    for i in x:
        yield i*2
def main(x=start):
    n=int(input())
    size=2*n
    while len(x)<n:
        x=tuple(gennext(x))
    for i in x[:-1]:
        print(i.strip().center(size)+' ')
    print(x[-1].strip().center(size))
if __name__=='__main__':
    main()
