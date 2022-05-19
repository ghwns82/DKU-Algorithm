import bisect as Q
I=input
M=257
R=range
m=map
H=[0]*M
x,y,b=m(int,I().split())
for _ in R(x):
  for i in m(int,I().split()):H[i]+=1
T=lambda p:sum(m(lambda h,n:n*(2*(h-p) if h>p else p-h),R(M),H))
A=list(R(0,min((b+sum(m(int.__mul__,R(M),H)))//(x*y),256)+1))
h=A[Q.bisect_right(A,type('',(),{'__lt__':lambda s,o:T(o-1)<T(o)})())-1]
print(T(h),h)
