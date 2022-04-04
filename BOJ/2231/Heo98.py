import sys
input=sys.stdin.readline

def find_og(N):
    str_num=str(N)
    for i in range(len(str_num)):
        N+=int(str_num[i])
    return N
def check(N):
    for i in range(1,N+1):
        if N==find_og(i):
            return i
    return 0

def main():
    N=int(input())
    ans=check(N)
    print(ans)



if __name__=="__main__":
    main()


