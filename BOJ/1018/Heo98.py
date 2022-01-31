M,N=map(int, input().split())
left_black=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]*4
left_white=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]*4
house_mat=[]
for idx in range(M):
    line=list(input())
    house_mat.append(line)

min_count=100000
count=0

for M_idx in range(M-7): 
    for N_idx in range(N-7):
        for chk in range(2):
            count=0
            if chk==0:# black
                for mov_down in range(8):
                    for mov_right in range(8):
                        if left_black[mov_down][mov_right]!=house_mat[M_idx+mov_down][N_idx+mov_right]:
                            count+=1
                if min_count>=count:
                    min_count=count
            else:
                for mov_down in range(8):
                    for mov_right in range(8):
                        if left_white[mov_down][mov_right]!=house_mat[M_idx+mov_down][N_idx+mov_right]:
                            count+=1
                if count<min_count:
                    min_count=count


print(min_count)
