#1
def f1(list):
    if len(list) == 0:
        return 0
    return list[0]+f1(list[1:])

# f1([1,2,3,4]) 
# f1([]) 

#2
def f2(n):   
    if n == 1:
        return 1
    elif n%2==0:        
        return 1 + f2(n//2)        
    else:
        return 1 + f2(3*n + 1)

# f2(637228127) 
# f2(11)
# f2(6)
# f2(1)

#3
def f3(list):
    if len(list) == 0:
        return
    else:
        print(list[-1])
        return f3(list[:-1])

# f3([1,2,3])
# f3([])
# f3([3,2,1])
#4
def f4(list):
    if len(list)==0:
        return
    else:
        v = list[0]
        if v%2 !=0 :
            print(v*3)
        f4(list[1:])

# f4([1,2,3,4])
# f4([2,4])
# f4([11,42,63,15])

#5
def f5(list):
    if len(list) == 0:
        return
    last = list[-1]
    if last % 2 !=0:
        last = last*3
    print(last)
    f5(list[:-1])

# f5([1,2,3,4])
# f5([2,4])
# f5([11,42,64,15])

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

# f10([1,2,3]) 
# f10([])

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


def f13(n):
  if n<=9:
    return 1
  else:
    count= 1+ f13(n//10)
    return count
# f13(0)

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

# f15([1,2,3]) 
# f15([2,4]) 
# f15([1,3,6,9]) 

def f16(list):
    res = []
    if len(list)==0:
        return res
    if list[0] % 2 ==1:
        return list[:1]+f16(list[1:])
    else:
        return f16(list[1:])

# f16([1,3,5,7]) 
# f16([1,2,3,4,5]) 

def f17(list):
    if len(list)==2:
        return list[0]
    return f17(list[1:])


def f18(a,b):
  x= a % b 
  if x == 0 :
    return b
  else:
    return f18(b,x)



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
        
# f19([1,2,3],[4,5]) 
# f19([4,5],[1,2,3]) 
# f19([],[1,2,3]) 
# f19([1,2,3],[]) 

def f20(lst):    
    half = len(lst)//2
    if len(lst) <= 1:
        return lst
    nlist1 = f20(lst[:half])
    nlist2 = f20(lst[half:])
    return f19(nlist1,nlist2)

# f20([5,3,1,2,4,6])
# f20([])
# f20([3,2,1])   








        

    


    
    


    


    



