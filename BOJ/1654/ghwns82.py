# 1654


k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]


def cal_length(i):
    result=0
    for line in lines:
        result+= line//i
    return result

left = 1
right = max(lines)
candidate=set()

while left<= right:
    mid = (left+ right)//2
    result = cal_length(mid)
    if result < n:
        right = mid-1
        
    else:
        left = mid +1
        candidate.add(mid)
print(max(candidate))
# print(right)
