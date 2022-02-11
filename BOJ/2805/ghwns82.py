# 2805

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def cal_height(h):
    result = 0
    for tree in trees:
        if tree > h:
            result+= (tree-h)
    return result

left = 0
right = max(trees)

candidate = []
while left <= right:
    mid = (left+right)//2
    result = cal_height(mid)

    if  result == m:
        print(mid)
        break
    elif result > m:
        left = mid+1
        candidate.append(mid)
    else:
        right = mid-1
else:
    print(max(candidate))
