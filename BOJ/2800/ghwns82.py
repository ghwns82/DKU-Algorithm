# 2800
line = input()
stack = []
pair = []
for i,v in enumerate(line):
    if v =='(':
        stack.append(i)
    if v==')':
        pair.append([stack.pop(), i])
result = [line]
for s,e in pair:
    new_result=[*result]
    for sen in result:
        l=list(sen)
        l[s]=' '
        l[e]=' '
        new_result.append(''.join(l))
    result = new_result
print(*sorted(list(set([r.replace(' ','') for r in result[1:]]))), sep='\n')
