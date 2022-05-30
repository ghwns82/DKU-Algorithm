import sys

N1, N2 = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N1+1, 1)]
N = 1
for i in range(N1, N1-N2, -1):
    N*=i

result = []
def N_M(i, S):
    global result

    if(len(result)!=N):
        if(len(S)==N2):
            result.append(S)
        else: 
            for j in range(i, len(arr), 1):
                if arr[j] not in S: #promising하게 만들어줌
                    N_M(0, S+[arr[j]])
    else:
        return result

N_M(0, [])
for a in result:
    for aa in a[:-1:]:
        print(aa,end=" ")
    print(a[-1])
