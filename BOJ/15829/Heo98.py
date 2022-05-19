import sys

input=sys.stdin.readline

def Hashing(str_,r,M):
    sum_=0
    for i in range(len(str_)):
        sum_+=((ord(str_[i])-96)*pow(r,i))
    print(sum_%M)


def main():
    N=int(input())
    r=31
    M=1234567891
    str_=input().strip()
    Hashing(str_,r,M)

if __name__=="__main__":
    main()
