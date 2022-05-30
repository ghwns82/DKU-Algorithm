import sys

input=sys.stdin.readline

str_ = list(input())

i = 0
start = 0

while i < len(str_):
    if str_[i] == "<":   
        i += 1 
        while str_[i] != ">":     
            i += 1 
        i += 1              
    elif str_[i].isalnum(): 
        start = i
        while i < len(str_) and str_[i].isalnum():
            i+=1
        tmp = str_[start:i] 
        tmp.reverse()       
        str_[start:i] = tmp
    else:                   
        i+=1                

print("".join(str_))
