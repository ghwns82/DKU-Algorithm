import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

    
def merge_sort(arr): 
    if len(arr)<=1: 
        return arr 
    
    mid = len(arr)//2 
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    low, high = 0, 0
    merged_arr=[]
    while low < len(left_arr) and high < len(right_arr): 
        if left_arr[low] < right_arr[high]:
            merged_arr.append(left_arr[low]) 
            low+=1 
        else: 
            merged_arr.append(right_arr[high])
            high+=1
    merged_arr += left_arr[low:]
    merged_arr += right_arr[high:]
    
    return merged_arr

result=merge_sort(arr)

for i in result:
    print(i)
