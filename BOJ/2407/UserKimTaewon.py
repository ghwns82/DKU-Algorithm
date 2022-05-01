from functools import reduce
def C(n,r):
    r=max(r,n-r)
    return reduce(int.__mul__,range(r+1,n+1))//reduce(int.__mul__,range(1,n-r+1))
def main():
    n,r=map(int,input().split())
    print(C(n,r))
if __name__=='__main__':
    main()
