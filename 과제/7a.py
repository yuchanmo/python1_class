#1
def f1(list):
    if len(list) == 0:
        return 0
    return list[0]+f1(list[1:])

#2
def f2(n):   
    if n == 1:
        return 1
    elif n%2==0:        
        return 1 + f2(n//2)        
    else:
        return 1 + f2(3*n + 1)


#3
def f3(list):
    if len(list) == 0:
        return
    else:
        print(list[-1])
        return f3(list[:-1])

#4
def f4(list):
    if len(list)==0:
        return
    else:
        v = list[0]
        if v%2 !=0 :
            print(v*3)
        f4(list[1:])

#5
def f5(list):
    if len(list) == 0:
        return
    last = list[-1]
    if last % 2 !=0:
        last = last*3
    print(last)
    f5(list[:-1])

#6 조교님이 풀어주신 솔루션
def f6(lst):
    if lst:            
        if type(lst[0])==list:
            return f6(lst[0])+f6(lst[1:])
        else:
            return lst[:1]+f6(lst[1:])
    else:
        return []

#7
def f7(n):
    if n == 0 :
        return 2
    elif n == 1 :
        return 1
    else:
        return f7(n-1) + f7(n-2)

#8
def f8(s):
    if len(s)<=1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        return f8(s[1:-1])
            



#9
def f9(n):
    if n == 0:
        return 1
    return n * f9(n-1)

#10
def f10(list):
    if len(list)==0:
        return 0
    return 1 + f10(list[1:])

#11
def f11(list):
    if len(list)==0:
        return 
    if len(list) == 1:
        return list[0]
        
    return f11(list[1:])

#12
def f12(n):
    if n == 0 :
        return
    print(n)
    return f12(n-1)

#13
def f13(n):
    if n == 0:
        return 1
    else:
        v = n//10
        if v == 0:
            return 1
        else:
            return 1 + f13(n//10)


#14
def f14(list):
    if len(list) == 0:
        return 
    if list[0]%2 == 1:
        return list[0]
    return f14(list[1:])


#15
def f15(list):
    if len(list)==0:
        return 0
    if list[0]%2 == 1:
        return list[0]+f15(list[1:])
    else:
        return f15(list[1:])


def f16(list):
    res = []
    if len(list)==0:
        return res
    if list[0] % 2 ==1:
        return list[:1]+f16(list[1:])
    else:
        return f16(list[1:])


def f17(list):
    if len(list)==2:
        return list[0]
    return f17(list[1:])


def f18(a,b):   
    if b>a:
        a,b = b,a
    if a-b == 0:
        return b
    return f18(a-b,b)

  

    


#f18 loop form
def test(a,b):
    d = 2
    s = 1
    while True:
        if a//d == 0 or b//d == 0:
            print(s)
            break
        if a%d ==0 and b%d==0:
            s = s*d
            a = a//d
            b = b//d
        else:
            d += 1




def f19(list1,list2):
    if len(list1) == 0:
        return list2
    elif len(list2) ==0:
        return list1
    else:
        if list1[0] < list2[0]:
            return list1[:1] + f19(list1[1:],list2)
        else:
            return list2[:1] + f19(list1,list2[1:])
        


def f20(lst):    
    half = len(lst)//2
    if len(lst) <= 1:
        return lst
    nlist1 = f20(lst[:half])
    nlist2 = f20(lst[half:])
    return f19(nlist1,nlist2)







        

    


    
    


    


    



