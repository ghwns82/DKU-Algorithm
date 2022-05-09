import sys

N1=int(sys.stdin.readline())
arr1=sys.stdin.readline().split()
N2=int(sys.stdin.readline())
arr2=sys.stdin.readline().split()

def binary_search(arr, num):
    low=0
    high=len(arr)-1
    while (low<=high):
        mid=(low+high)//2
        if(arr[mid]==num):
            return mid
        elif(arr[mid]>num):
            high=mid-1
            continue
        elif(arr[mid]<num):
            low=mid+1
            continue
            
    return -1

arr1=sorted(arr1)
for i in arr2:
    is_in=binary_search(arr1, i)
    if(is_in==-1):
        print(0)
    else:
        print(1)
