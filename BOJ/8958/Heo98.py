num=int(input())
sum_=[]
for index in range(num):
    solve=input()
    continuous=0
    sum_.append(0)
    for k in solve:
        if k=='O':
            continuous+=1
            sum_[index]+=continuous
        else:
            continuous=0
for index in range(num):
    print(sum_[index])
