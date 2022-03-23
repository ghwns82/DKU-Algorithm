#이론상 위의 UserKimtaewon.py와 같이 동작해야 하나, 제출하였을 경우 틀린다.
def get_va_line():
    n_item,*items=map(int,input().split(' '))
    assert len(items)==n_item
    return items

def main():
    global trues,false_parties,newtrues
    n,m=map(int,input().split(' '))

    trues=get_va_line()
    trues=set(trues)

    false_parties=set(frozenset(get_va_line()) for _ in range(m))

    while trues:
        newfalse_parties=set(false_parties)
        newtrues=set(trues)
        for p in tuple(false_parties):
            if not trues.isdisjoint(p):
                newtrues.update(p)
                newfalse_parties.remove(p)
        false_parties=newfalse_parties
        trues=newtrues-trues
    print(len(false_parties))

if __name__=='__main__':
    main()
