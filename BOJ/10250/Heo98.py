import sys

input=sys.stdin.readline
# Y= H로 구분 X는 W

def Hotel(H,W,N):
    floor_=N%H
    room_num=N//H+1
    if N%H==0:
        floor_=H
        room_num-=1
    print(f'{floor_}{room_num:02d}')
def main():
    T=int(input())
    for i in range(T):
        H,W,N=map(int, input().split())
        Hotel(H,W,N)

if __name__=="__main__":
    main()
    
    
