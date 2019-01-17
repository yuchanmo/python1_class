def p41(lst):
    res = []
    for i in lst:
        if i%2 == 1:
            res.append(i)
    return res

p41([1,2,3,4])


def f46(lst):
    assert lst != []
    maxval = lst[0]
    for i in lst[1:]:
        if i > maxval :
            maxval = i
    return maxval



f46([1,2,100,3,33,4,5,64,])


def f49(w,h):
    list(map(print,['*'*w]*h))

f49(5,6)


def f410(n):
    list(map(lambda x : print('*'*int(x)),range(n)))

f410(10)

import functools as f

def f25(n):
    if n < 10:
        return n
    
    while n > 10:
        n  = n //10
    return n


f25(123523)
f25(53445)
f25(324324234234)

def f26(lst):
    res = []
    for o in lst:
        l = o[0]
        for i in o[1:]:
            if i > l:
                l = i
        res.append(l)
    return res

f26([[22,1,2,3],[4,44,5,6],[7,35,8,9]])
    
        
ll = [1,2,3,3,5,3,3,3,3,3,3,3]

ll.count(3)
ll.index(5)
print(ll)
ll.remove(3)
ll.clear()
print(ll)


s = []
for v in range(1,11):
    ss = v**2
    s.append(ss)
print(s)

lsls = ["zero","one","two","three","four"]
list(map(lambda x : (x.title()),lsls[1:3]))



def aa(n):
    list(map(lambda x : print(*range(1,x+1)),range(1,n+1)))

aa(5)


def aaa(n):
    c = 1
    for i in range(1,n+1):
        for j in range(0,i):
            print(c,end=' ')
            c+=1
        print()


def aaaa(n):
    list(map(lambda x : print(*range(1,x+1)),range(1,n+1)))

aaaa(6)




def fac(n):
    print("on handling %s"%(n))
    if n <=1 :
         return 1
    return n*fac(n-1)

fac(3)
        

aaa(5)



def fibo(n,depth=0):
    if n<=1:
        return n
    print('\t'*depth, n-1,n-2)
    d = depth +1
    return fibo(n-1,d) + fibo(n-2,d)

fibo(5)
0,1,1,2,3,5,8,13,21,34,55

def fibo2(n):
    x = 0
    next_x = 1
    for i in range(1,n+1):
        x,next_x = next_x, x + next_x
    return x

fibo2(7)


def qs(lst):
  if len(lst)>1:
    pi=len(lst)//2
    SL=[]
    LL=[]
    for i,v in enumerate(lst):
      if i != pi:
        if v<lst[0]:
          SL.append(v)
        else:
          LL.append(v)
    qs(SL)
    qs(LL)
    return SL+[lst[0]]+LL
    
qs([4,5,3,6,9,8,7])