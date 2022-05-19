# 1931
meetings = [list(map(int, input().split())) for _ in range(int(input()))]
meetings = sorted(meetings, key=lambda a: a[0])
meetings = sorted(meetings, key=lambda a: a[1])
end = meetings[0][1]
cnt=1
for meet in meetings[1:]:
    if meet[0]>=end:
        cnt+=1
        end=meet[1]
print(cnt)
