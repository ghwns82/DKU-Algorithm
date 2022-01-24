empty_li=[]
for i in range(10):
    a=int(input())
    if a%42 not in empty_li:
        empty_li.append(a%42)
print(len(empty_li))
