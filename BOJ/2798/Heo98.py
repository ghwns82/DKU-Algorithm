import sys

# 무조건 3개 선택이고
# N은 카드 개수 M은 우리가 만들고자 하는 수

input=sys.stdin.readline


def black_jack(N,M,list_):
    sum_list=[]
    for i in range(0,N-2):
        for k in range(i+1,N-1):
            for j in range(k+1,N):
                sum_=list_[i]+list_[k]+list_[j]
                if sum_<=M:
                    sum_list.append(sum_)
    print(max(sum_list))

def main():
    N,M = map(int, input().split())
    list_=list(map(int,input().split()))
    black_jack(N,M,list_)
    

if __name__=="__main__":
    main()
