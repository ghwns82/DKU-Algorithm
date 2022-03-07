# 1541
line = input()
temp=''
temp2=''
new_line=''
for c in line:
    if not c.isdigit():
        new_line+=str(int(temp2))
        temp2=''
        if temp!='(' and c =='-':
            new_line+='-('
            temp='('
        elif temp=='(' and c=='-':
            new_line+=')-('
#             temp=')'
        elif temp=='(' and c=='+':
            new_line+=c
        else:
            new_line+=c
    else:
        temp2+=c
new_line+=str(int(temp2))
if temp=='(':
    new_line+=')'
print(eval(new_line))
