# 10830
import sys
input = sys.stdin.readline
# 10830
n, b = map(int, input().split())
matrix =[list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] %=1000
def cal_matrix(n, matrix1, matrix2):
    result = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+= matrix1[i][k] * matrix2[k][j]
                result[i][j] %= 1000                    
    return result

note = {}
def cal(N):
    if N == 1:

        return matrix
    elif N ==2:
        if str(N) in note.keys():
            return note[str(N)]
        note[str(N)] = cal_matrix(n, matrix, matrix)
        return note[str(N)] 
    else:
        if N%2:
            if str(N) in note.keys():
                return note[str(N)]
            note[str(N)] = cal_matrix(n, cal(N-1), matrix)
            return note[str(N)]
        else:
            if str(N) in note.keys():
                return note[str(N)]
            note[str(N)] = cal_matrix(n, cal(N//2), cal(N//2))
            return note[str(N)]
        
result = cal(b)
for i in result:
    print(*i)
