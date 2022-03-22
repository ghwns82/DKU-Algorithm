# 11053

n = int(input())
sequence=list(map(int, input().split()))
result=[0]*n
result2=[0]*n
for i,v in enumerate(sequence):
    for j in sorted(zip(result[:i],sequence[:i]), reverse=True):
        if j[1]<v:
            result[i] = j[0]+1
            break
for i,v in enumerate(sequence[::-1]):
    for j in sorted(zip(result2[:i],sequence[::-1][:i]),reverse=True):
        if j[1]<v:
            result2[i] = j[0]+1
            break
for i,v in enumerate(result):
    result[i]+=result2[n-1-i]
print(max(result)+1)
