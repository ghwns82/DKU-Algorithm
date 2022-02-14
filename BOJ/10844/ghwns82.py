def cal(depth, num):
    if depth==1:
        return 1
    else:
        if 0<num<9:
            return cal(depth-1, num-1)+cal(depth-1, num+1)
        if num==9:
            return cal(depth-1, num-1)
        if num ==0:
            return cal(depth-1, num+1)
depth = int(input())
result=0
for i in range(1,10):
    result += cal(depth, i)
print(result)
