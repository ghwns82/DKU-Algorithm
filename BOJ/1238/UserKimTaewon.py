from functools import partial

RoadData=list[list[tuple[int,int]]]

def makedct(m:int,n:int)->tuple[RoadData,RoadData]:
    invdct=[[] for _ in range(n)]
    dct=[[] for _ in range(n)]
    for _ in range(m):
        st,ed,t=map(int,input().split())
        st-=1
        ed-=1
        dct[st].append((ed,t))
        invdct[ed].append((st,t))
    return dct,invdct

def main():
    n,m,x=map(int,input().split())
    dct,invdct=makedct(m,n)
    x-=1
    distf=partial(getdists,m,n,x)
    print(max(map(int.__add__,distf(dct),distf(invdct))))

def getdists(m:int,n:int,x:int,roaddata:RoadData):
    checking={x}
    check=set()
    xdist=[None for _ in range(n)]
    xdist[x]=0
    while checking:
        for st in checking:
            stt=xdist[st]
            assert stt is not None
            for ed,t in roaddata[st]:
                edt=t+stt
                if xdist[ed] is None or xdist[ed]>edt:
                    xdist[ed]=edt
                    check.add(ed)
        check,checking=checking,check
        check.clear()
    return xdist

if __name__=='__main__':
    main()
