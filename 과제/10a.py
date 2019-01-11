from functools import reduce

def f1(lst):
    return len(list(filter(lambda x:x%2==1,lst)))

# f1([1,2,3,4])
# f1([1,2,3,4,5])

def f2(lst):
    for i in filter(lambda x : x%2 ==1, lst):
        print(i)

# f2([1,2,3,4])
# f2([1,2,3,4,5])

def f3(lst):
    return sum(filter(lambda x:x%2==1,lst))
    # return reduce(lambda x,y:x+y,filter(lambda x:x%2==1,lst))


# f3([1,2,3,4,5])
# f3([1,2,3,4])

def f4(lst):
    sum = 0
    for i,v in enumerate(lst):
        if v%2==1:
            sum+=i
    return sum
    # return sum([i for i,v in enumerate(lst) if v%2 ==1])

# f4([1,2,3,4])
# f4([1,2,3,4,5])


def f5(lst):
    return list(map(lambda x:x**2,lst))

# f5([1,2,3,4])
# f5([1,2,3,4,5])


def f6(lst):
    return max(lst)

# f6([1,2,3,4])
# f6([1,2,3,4,5])

def f7(lst):
    return sum(lst)/len(lst)

# f7([1,2,3,4])
# f7([1,2,3,4,5])

def f8(a,b,n):
    list(map(print,filter(lambda x : x % n ==0, range(a,b+1))))
    # for v in filter(lambda x : x % n ==0, range(a,b+1)):
    #     print(v)

# f8(1,10,2)

def f9(width,height):
    list(map(print,['*'*width]*height))

# f9(0,1)
# f9(10,0)
# f9(1,1)
# f9(5,5)

def f10(n):
    lst = list(range(1,n+1))
    list(map(print,map(lambda x:'*'*x,lst)))


# f10(1)
# f10(2)
# f10(3)

def f11(lst):
    return sorted(lst,reverse = True) == lst

# f11([])
# f11([5,4,3,2,1])
# f11([5,4,3,2,0])
# f11([5,4,5,2])