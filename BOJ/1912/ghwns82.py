n=int(input())

sequence = list(map(int, input().split()))

sum_ = sequence[0]
min_ = sum_
sum_seq=[sum_]
for i in sequence[1:]:
    
    min_ = min(min_, sum_)
    sum_+=i
    sum_seq.append(max(sum_-min_, sum_))
print(max(sum_seq))
