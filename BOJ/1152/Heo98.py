sentence=input()
count=0
if sentence == '':
    count=0
elif len(sentence)==1 and sentence==" ":
    count=0
else:
    for index,i in enumerate(sentence):  
        if index==0 and i ==" ":
            count+=0
        elif index==int(len(sentence)-1) and i ==" ":
            count +=0
        elif i==" ":
            count+=1
    count+=1

print(count)
