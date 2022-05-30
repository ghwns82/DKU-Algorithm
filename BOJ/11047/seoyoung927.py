import sys

N, amount = map(int, sys.stdin.readline().split())
S = list(reversed([int(sys.stdin.readline()) for _ in range(N)]))

def greedy(S, amount):
    total_cnt=0
    cur_amt=0
    idx=-1

    while True:
        #선택 과정
        idx+=1
        tmp=S[idx]
        
        #적절성 확인
        if(tmp+cur_amt<=amount):
            cur_cnt=((amount-cur_amt)//tmp) 
            total_cnt+=cur_cnt
            cur_amt+=tmp*cur_cnt

        #해답 검사
        if(cur_amt==amount):
            break

    return total_cnt

print(greedy(S, amount))
