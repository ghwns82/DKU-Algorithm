origin_num=list(map(int,input().split()))
sum_value=0
for i in origin_num:
    sum_value+=i**2
print(sum_value%10)    
