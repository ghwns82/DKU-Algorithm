#피보나치 수열의 일반항 공식을 사용하였다.
#fib(n)=((1+sqrt5)**n-(1-sqrt5)**n)/(sqrt5*2**n)
#(단,이 공식에서 sqrt5는 5의 제곱근이다)

M=1_000_000_007
inv2=500000004

assert (2*inv2)%M==1

def mypow2(real:int,pow5:int)->tuple[int,int]:
    return (real**2+5*pow5**2)%M,(2*real*pow5)%M

def mypow(real:int,pow5:int,n:int)->tuple[int,int]:
    if n==0:
        return 1,0
    if n==1:
        return real,pow5
    if n%2==0:
        return mypow2(*mypow(real,pow5,n//2))
    else:
        newreal,newpow5=mypow2(*mypow(real,pow5,n//2))
        return (newreal*real+5*pow5*newpow5)%M,(newreal*pow5+real*newpow5)%M

def fib(n:int)->int:
    _,p1=mypow(1,1,n)
    _,p2=mypow(1,-1,n)
    return ((p1-p2)*pow(inv2,n,M))%M
    
n=int(input())
print(fib(n))
