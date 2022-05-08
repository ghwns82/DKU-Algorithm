def get_va_line():
    n_item,*items=map(int,input().split(' '))
    assert len(items)==n_item
    return items

def get_filter(trues,newtrues):
    def filter(p):
        if not trues.isdisjoint(p):
            newtrues.update(p)
            return False
        return True
    return filter

def main():
    #global trues,false_parties,newtrues #디버그를 위해 쓰던 수단
    
    n,m=map(int,input().split(' '))

    trues=get_va_line()
    trues=set(trues)

    false_parties=tuple(frozenset(get_va_line()) for _ in range(m))
    
    
    while trues:
        newtrues=set(trues)
        #for p in [*false_parties]:
        #    if not trues.isdisjoint(p):
        #        false_parties.remove(p)
        #        newtrues.update(p)
        # 왠지 모르게 이걸 이용하여 false_parties에서 거짓말을 할 수 없는 파티를 제거할 때는 문제가 틀리다 get_filter와 filter를 사용하니 문제가 풀렸다. 대체 왜?
        f=get_filter(trues,newtrues)
        false_parties=tuple(filter(f,false_parties))
        trues=newtrues-trues
    print(len(false_parties))

if __name__=='__main__':
    main()
