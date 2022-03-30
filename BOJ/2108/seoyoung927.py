import sys

N=int(sys.stdin.readline())
arr=sorted([int(sys.stdin.readline()) for i in range(N)])
#산술평균
print(round(sum(arr)/len(arr)))
#중앙값
print(arr[len(arr)//2])
#최빈값
max_cnt=1
cnt=1
tmp=[arr[0]]
for i in range(1, len(arr), 1):
    if(arr[i-1]==arr[i]):
        cnt+=1
    else:
        cnt=1
    if(cnt>max_cnt):
        max_cnt=cnt
        tmp=[]
        tmp.append(arr[i])
    elif(cnt==max_cnt):
        tmp.append(arr[i])
    else:
        continue
if(len(tmp)==1):
    print(tmp[0])
else:
    print(tmp[1])
#최대값-최소값
print(max(arr)-min(arr))
