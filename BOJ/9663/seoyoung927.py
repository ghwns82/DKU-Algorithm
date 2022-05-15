import sys

N=int(sys.stdin.readline())

#col은 i번째 행에 있는 여왕말이 놓여 있는 열
col=[0 for i in range(N)]

cnt=0
def queens(i):
    if promising(i) or i==-1:
        #i번째 행이 유망하면
        #i+1째 행에 어떤 열에 queen을 놓을지 결정
        if(i==N-1):
            global cnt
            cnt+=1
            return 0
        else:
            if i==0 and N%2==0:
                for j in range(0,N//2):
                    col[i+1]=j
                    queens(i+1)
            else:
                for j in range(0,N):
                    col[i+1]=j
                    queens(i+1)
    


def promising(i):
    idx=0
    switch=True
    while(idx<i and switch):
        if(col[i]==col[idx] or abs(col[i]-col[idx])==i-idx):
            switch=False
        idx+=1
    return switch

queens(-1)
if N%2==0:
    print(cnt*2)
else:
    print(cnt)
