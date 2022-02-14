n, m, b = map(int, input().split())
yard = []
for _ in range(n):
    yard += list(map(int, input().split()))
ans = 10000000000000000000000
max_h = 0
for i in range(min(yard), (sum(yard)+ b)//(n*m)+1):
    result = 0
    for j in yard:
        if j>i:
            result+=(j-i)*2
        else:
            result+= (i-j)    
    if ans>=result:
        ans = result
        max_h=i

print(ans, max_h)
