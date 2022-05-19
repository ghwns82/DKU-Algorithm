from itertools import count

def backward(end,start):
    for i in count(1):
        if end==start:
            return i
        if end<start:
            return -1
        elif end%2==0:
            end//=2
        elif end%10==1:
            end//=10
        else:
            return -1
def main():
    st,ed=map(int,input().split())
    print(backward(ed,st))
if __name__=='__main__':
    main()
