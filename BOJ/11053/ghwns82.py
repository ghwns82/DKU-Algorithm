# 11053

n = int(input())
sequence=list(map(int, input().split()))
result=[0]*n
for i,v in enumerate(sequence):
    for j in sorted(zip(result[:i],sequence[:i]), reverse=True):
        if j[1]<v:
            result[i] = j[0]+1
            break
print(max(result)+1)
