#2981
nums = [int(input()) for i in range(int(input()))]

gcd = abs(nums[0]-nums[1])
for i in range(len(nums)-1):
    num = abs(nums[i]-nums[i+1])
    while num%gcd:
        num, gcd = gcd, num%gcd
        
result=set()
for i in range(2, int(gcd**0.5)+1):
    if gcd%i==0:
        result.add(i)
        result.add(gcd//i)
result.add(gcd)
print( *sorted(list(result)), sep=' ')
