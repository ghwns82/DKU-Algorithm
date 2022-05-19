import sys

input=sys.stdin.readline    

M=int(input())
list_=[]
for i in range(M):
    what_list=input().strip().split()
    what_=what_list[0]
    try:
        num_=int(what_list[1])
    except:
        pass
    if what_=='add':
        if num_ not in list_:
            list_.append(num_)
    elif what_== 'remove':
        if num_ in list_:
            list_.remove(num_)
    elif what_=="check":
        if num_ in list_:
            print(1)
        else:
            print(0)
    elif what_=='toggle':
        if num_ in list_:
            list_.remove(num_)
        else:
            list_.append(num_)
    elif what_ =="all":
        list_=[x for x in range(1,21)]
    elif what_=='empty':
        list_=[]
