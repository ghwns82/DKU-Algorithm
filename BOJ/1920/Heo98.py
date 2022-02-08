import sys
input=sys.stdin.readline

N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))
N_list.sort()
for ele in M_list:
    chk=0
    start=0
    end=len(N_list)-1
    while(chk!=1):
        mid=(start+end)//2 
        if start>end:
            print("0")
            chk=1
        if N_list[mid]==ele:
            print("1")
            chk=1
        elif N_list[mid]>ele:
            end=mid-1
        else:
            start=mid+1
