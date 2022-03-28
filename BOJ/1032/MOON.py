n = int(input())
a = list(input()) 
aLen = len(a) 

for i in range(n-1):
    b = list(input()) 
    for j in range(aLen):
        if a[j] != b[j]: 
            a[j] = '?' 
print(''.join(a))
