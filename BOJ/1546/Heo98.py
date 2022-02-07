N=int(input())
sub_list=list(map(int,input().split()))
max_value=sub_list[0]
for i in range(N):
    if max_value<sub_list[i]:
        max_value=sub_list[i]
sum_value=0
for i in range(N):
    sum_value+=sub_list[i]/max_value*100
print(sum_value/N)
      

