Data=list[tuple[int,int,int]]

def reduce(arr:Data,f):
    arr=iter(arr)
    i0,j0,k0=next(arr)
    for i,j,k in arr:
        i0,j0,k0=f(i0,j0)+i,f(i0,j0,k0)+j,f(j0,k0)+k
    return f(i0,j0,k0)

def main():
    N=int(input())
    data:Data=[tuple(map(int,input().split())) for _ in range(N)]
    print(reduce(data,max),reduce(data,min))

if __name__=='__main__':
    main()  
