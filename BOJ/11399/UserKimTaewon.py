from itertools import accumulate
def main():
    input()
    print(sum(accumulate(sorted(map(int,input().split())))))
if __name__=='__main__':
    main()
