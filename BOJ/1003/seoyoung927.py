# 피보나치 함수
import sys

N=int(sys.stdin.readline())

count_zero={0:1, 1:0}
def opt_zero(num):
    for n in range(0,num+1):
        if n not in count_zero:
            count_zero[n]=count_zero[n-1]+count_zero[n-2]
    return count_zero[n]

count_one={0:0, 1:1}
def opt_one(num):
    for n in range(0,num+1):
        if n not in count_one:
            count_one[n]=count_one[n-1]+count_one[n-2]
    return count_one[n]

for _ in range(N):
    num = int(sys.stdin.readline())
    print(opt_zero(num), opt_one(num))
