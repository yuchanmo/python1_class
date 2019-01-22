def sum(a,b):    
    print(__name__)
    return a+b


def safe_num(a,b):
    if type(a) != type(b):
        print('더 잘할수 있는 것 아닙니다')
        return
    else:
        result = sum(a,b)
    return result



if __name__=='__main__':
    print(safe_num('a',1))
    print(safe_num(1,4))
    print(sum(10,10.4))




