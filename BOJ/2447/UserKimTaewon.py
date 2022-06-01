def manger_next(prev):
    for i in prev:
        yield i*3
    for i in prev:
        leni=len(i)
        yield i+' '*leni+i
    for i in prev:
        yield i*3
def main(start=('*',)):
    n=int(input())
    x=start
    while len(x)<n:
        x=tuple(manger_next(x))
    for i in x:
        print(i)
if __name__=='__main__':
    main()
