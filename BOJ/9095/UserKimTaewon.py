def add(table):
    table.append(sum(table[-3:]))
def way(x,table=[1,1,2]):
    if x<len(table):
        return table[x]
    else:
        for _ in range(x-len(table)+1):
            add(table)
        return table[x]
if __name__=='__main__':
    for _ in range(int(input())):
        print(way(int(input())))
