S=input().lower()
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
order_li=[-1]*26
for k in alpha:
    if k in S:
        order_li[alpha.index(k)]=S.index(k)
for i in order_li:
    print(i,end=" ")
