N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
students = [[0] * N for _ in range(N)]       

for i in range(5):
    grade = []
    for j in range(N):
        grade.append(data[j][i])
    for j in range(len(grade)):
        if grade.count(grade[j]) > 1:
            for k in range(len(grade)):
                if grade[j] == grade[k] and k != j:
                    students[j][k] = 1

li = [sum(student) for student in students]
max_value = max(li)
result = li.index(max_value) + 1

print(result)
