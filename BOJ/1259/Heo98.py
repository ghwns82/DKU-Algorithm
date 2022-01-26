solve_list=[]
while(True):
    a=str(input())
    if a[0]=='0':
        break
    if a== a[::-1]:
        solve_list.append('yes')
    else:
        solve_list.append('no')
for i in solve_list:
    print(i)
