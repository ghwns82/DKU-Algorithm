from itertools import combinations_with_replacement
def main():
    N,M=map(int,input().split())
    nums=sorted(map(int,input().split()))
    for i in combinations_with_replacement(nums,M):
        print(' '.join(map(str,i)))

if __name__=='__main__':
    main()
