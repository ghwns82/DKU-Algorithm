# 짧은순으로
# 사전순
num=int(input())
dictionary_list=[]
for i in range(num):
    k= input()
    if k not in dictionary_list:
        dictionary_list.append(k)

dictionary_list.sort()
dictionary_list.sort(key = lambda x : len(x))

for i in dictionary_list:
    print(i)
