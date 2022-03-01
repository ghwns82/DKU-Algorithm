n = int(input())
dead = [0 for i in range(n+1)]
now = 0
result=''
for _ in range(n):
    target = int(input())
    if dead[target]:
        print('NO')
        break
    if target == now:
        result+='-'
        dead[target]+=1
        now-=1
    elif target > now:
        result+='+'*(target-sum(dead[now+1:target+1])-now) + '-'
        dead[target]+=1
        now = target-1
    else:
        result+='-'*(now-sum(dead[target+1:now+1])-target+1)
        dead[target:now+1] = [1]* (now-target+1)
        now = target-1
else:
    print('\n'.join(result))
