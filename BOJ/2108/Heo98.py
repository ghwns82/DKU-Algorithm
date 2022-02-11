# N은 홀수
import sys
import statistics
from collections import Counter
input=sys.stdin.readline
N=int(input())
num_list=[int(input()) for _ in range(N)]
num_list.sort() # list 자체를 바꿔줌
print(int(round(sum(num_list)/len(num_list),0)))
print(num_list[len(num_list)//2])
cnt=Counter(num_list).most_common(2) # sort라서 작은 수부터 가져옴.

if len(num_list)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(num_list)-min(num_list))

