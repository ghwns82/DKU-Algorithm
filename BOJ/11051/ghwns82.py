#11051
n,k=map(int, input().split())
k = min(k, n-k)
result=1
for i in range(k):
    result *= n-i
for i in range(k):    
    result //= i+1
print(int(result)%10007)
