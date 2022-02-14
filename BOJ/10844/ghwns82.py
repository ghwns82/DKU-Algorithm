# 10844
state=[0]+[1 for i in range(9)]
for _ in range(int(input())-1):
    next_state = [0 for i in range(10)]
    for i,v in enumerate(state[1:-1],1):
        next_state[i+1]+=v
        next_state[i-1]+=v
    next_state[1]+=state[0]
    next_state[8]+=state[9]
    state = next_state
print(sum(state)%1_000_000_000)
