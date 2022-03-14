n,m = map(int,input().split())
h = list(map(int,input().split()))

right=max(h)
left =1

while(left <= right):
    mid = (left+right)//2
    get_trees =0
    for i in h:
        if(i>mid):
            get_trees+=(i-mid)
    if(get_trees>=m):
        left = mid+1
    else:
        right = mid-1

print(right)
