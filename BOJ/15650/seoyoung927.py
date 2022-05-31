import sys

# 초기 변수 설정
N1, N2 = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N1+1,1)]
N = 1
for i in range(N1,N1-N2,-1):
    N*=i
for i in range(1,N2+1,1):
    N=N//i

result=[]
def N_M(i,S):
    global result

    if(len(result)!=N):
        if(len(S)==N2):
            result.append(S)
        else:
            for j in range(i, len(arr), 1):
                if arr[j] not in S:
                    N_M(j+1,S+[arr[j]])
    else:
        return result

N_M(0,[])
for a in result:
    if(len(a)!=0):
        for aa in a[:-1:]:
            print(aa,end=" ")
        print(a[-1])
