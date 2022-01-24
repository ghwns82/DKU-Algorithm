word=input().upper()
char_list=list(word)
char_set=set(char_list)
dic=dict()
index=0
for i in char_set:
    count=0
    for k in char_list:
        if i == k:
            count+=1
    dic[i]=count
    if index==0:
        index=i
    else:
        if dic[index]<count:
            index=i
count=0
for key, value in dic.items():
    if value ==dic[index]:
        count+=1
if count>=2:
    print("?")        
else: print(index)
