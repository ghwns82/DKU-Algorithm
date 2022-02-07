A=int(input())
B=int(input())
C=int(input())
Multi=str(A*B*C)
for i in range(10):
    count=0
    for k in Multi:
        if i==int(k):
            count+=1
    print(count)
