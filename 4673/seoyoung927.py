def self_number(n):
    result=n
    while True:
        #한자리수이면 종료
        if(n//10==0):
            result+=n
            break
        result+=(n%10)
        n=n//10
    
    return result

ss=set([i for i in range(1,10001,1)])
for i in range(1,10001, 1):
    ss.discard(self_number(i))
for i in list(ss):
    print(i)
