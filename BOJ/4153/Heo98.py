import sys

input=sys.stdin.readline

def chk_right(a,b,c):
    list_=sorted([a,b,c])
    if a ==0 and b==0 and c ==0:
        return 1
    if (list_[0])**2+(list_[1]**2)==(list_[2]**2):
        print("right")
        return 0
    else:
        print("wrong")
        return 0
    
def main():
    while(1):
        a,b,c=map(int,input().split())
        chk=chk_right(a,b,c)
        if chk==1:
            break
if __name__=="__main__":
    main()
