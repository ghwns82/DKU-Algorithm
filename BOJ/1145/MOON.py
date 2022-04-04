a = list(map(int, input().split()))
m = min(a)
count = 0

while True:
    count = 0 
    for i in range(len(a)): 
        if m % a[i] == 0: 
            count += 1 
    if count >= 3: 
        print(m) 
        break
    m += 1 
