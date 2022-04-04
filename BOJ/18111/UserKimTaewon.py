from typing import List,Callable

def cost(avg:int,x:int)->int:
    diff=x-avg
    if diff>0:
        return 2*diff
    else:
        return -diff

def fst_nonzero(x:List[int])->int:
    for idx,it in enumerate(x):
        if it!=0:
            return idx

def get_eta(hdist:List[int],MAXH:int)->Callable[[int],int]:
    def eta(pivot:int):
        return sum(map(lambda h,n:n*cost(pivot,h),range(MAXH+1),hdist))
    return eta

def main(MAXH=256):
    hdist=[0 for _ in range(MAXH+1)]
    n,m,b=map(int,input().split())
    
    for _ in range(n):
        for i in map(int,input().split()):
            hdist[i]+=1

    blocks=b+sum(map(lambda h,n:h*n,range(MAXH+1),hdist))
    eta=get_eta(hdist,MAXH)
    
    minh=fst_nonzero(hdist)
    maxh=min(blocks//(m*n),MAXH)+1

    while minh<maxh:
        middle=(minh+maxh)//2
        meta=eta(middle)
        beta=eta(middle-1)

        if beta<meta:
            maxh=middle
        else:
            minh=middle+1
    h=minh-1
    
    print(eta(h),h)

if __name__=='__main__':
    main()
