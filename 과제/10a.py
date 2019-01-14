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

def f12(lst):
    return all(map(lambda x:x<0,lst))

# f12([])
# f12([-1,-2,-3,-4,5])
# f12([1,2,3,4,5])
# f12([-1,-2,-3])

def f13(lst,target):
    return max(list(map(lambda x : x[0],filter(lambda x : x[1] == True, enumerate(map(lambda x:x == target,lst))))))

# f13([1,2,3,1,2,3],3)
# f13([1,2,3],3)
# f13([1,1,1,1],1)

def f14(lst):
        return max(map(lambda l,i: -1 if l>=0 else i,lst,range(len(lst))))

# f14([1,2,-3])
# f14([1,-2,-3,1,-2,-3])
# f14([-1,1,1,1])

def f15(lst):
        return sum(map(lambda l,i:0 if i % 2 else l,lst,range(len(lst))))

# f15([1,2,-3])
# f15([1,-2,-3,1,-2,-3])
# f15([-1,1,1,1])

def f16(n):
        list(map(print,map(lambda x : '*'*x , range(n,0,-1))))

# # f16(3)
# # f16(2)
# # f16(1)

def f17(lst):
        list(map(lambda i : print(lst[i]),range(len(lst)-1,-1,-2)))

# f17([1,2,3,4,5,6])
# f17([1,2,3,4])
# f17([1])

def f18(n):
        print(reduce(lambda x,y:x*y,[1]+list(range(1,n+1))))

# f18(0)
# f18(2)
# f18(3)

def f19(matrix):
        list(map(lambda x : print(sum(x)),matrix))

# f19([[1,0],[0,1]])
# f19([[1,2,3],[4,5,6]])
# f19([[1],[2],[3],[4]])

def f20(matrix):
        list(map(lambda i : print(matrix[i][i]),range(len(matrix))))

# f20([[1,0],[0,1]])
# f20([[1,2,3],[4,5,6],[7,8,9]])
# f20([[1]])

def f21(lst):
        list(map(lambda x : print(reduce(lambda x,y : x*y ,range(1,x+1))),lst))

# f21([])
# f21([1,2,3])
# f21([1,2,3,4])

def f22(lst):
        list(map(lambda x : print(*range(x,-1,-1)),lst))

# f22([])
# f22([1,3,5])
# f22([5,3,6,2])


def f23(lst1,lst2):
        return list(map(lambda x,y:x+y,lst1,lst2))

# f23([],[])
# f23([1,2,3],[1,2,3])
# f23([0,0,0],[1,2,3])

def f24(n):
        list(map(print, filter(lambda x:x%2==0 or x%3==0,range(1,n+1))))

# f24(10)
# f24(1)
# f24(3)

def f25(lst):
        return max(map(lambda x:max(x) if x else 0,lst))

# f25([[1,2,3],[4,5,6],[7,8,9]])
# f25([[3,2,1],[0,-1,-2]])
# f25([[1,2,3,4],[],[34],[],[],[56],[67]])

def f26(lst):
        return list(sorted(lst,reverse = True))[1]

# f26([1,4,3,2,5])
# f26([3,2])
# f26([3,4])

#다시 풀어봐야할듯
def f27(n):
        return eval(str(n)[0])

# f27(1234)
# f27(5326)
# f27(3)

        

def f28(lst):
        list(map(lambda x : print(max(x)),lst))

# f28([[1,2,3],[4,5,6],[7,8,9]])
# f28([[3,2,1],[0,-1,-2]])
# f28([[1,2,3,4],[1],[34],[2],[3],[56],[67]])