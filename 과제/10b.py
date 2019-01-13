from functools import reduce

def f1(n):
    list(map(lambda x:print(*range(1,x+1)), range(1,n+1)))

#f1(5)

def f2(n):
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(1,n+1)))

# f2(0)
# f2(1)
# f2(5)

def f3(n):
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(1,n+1)))
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(n-1,0,-1)))

# f3(0)
# f3(1)
# f3(5)

def f4(n):
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(1,n+1)))
    list(map(lambda x:print(*range(1+sum(range(n))+x+1,1+sum(range(n+1))+x)), range(n-1,0,-1)))

f4(3)
f4(0)
f4(1)


def f5(matrix):
    list(map(lambda x:print(sum(x)),matrix))

# f5([[1,0],[0,1]])
# f5([[1,2,3],[4,5,6]])
# f5([[1],[2],[3],[4]])

def f6(matrix):
    return sum(map(sum,matrix))

# f6([[1,0],[0,1]])
# f6([[1,2,3],[4,5,6]])
# f6([[1],[2],[3],[4]])

def f7(matrix):
    return reduce(lambda a,b : a*b, reduce(lambda x,y:x+y,matrix))

# f7([[1,0],[0,1]])
# f7([[1,2,3],[4,5,6]])
# f7([[1],[2],[3],[4]])

def f8(matrix):
    list(map(lambda x : print(*list(filter(lambda y: y%2 ,matrix[x]))),range(len(matrix))))

# f8([[1,0],[0,1]])
# f8([[1,2,3],[4,5,6]])
# f8([[1],[2],[3],[4]])


def f9(matrix1,matrix2):
    return list(map(lambda m1,m2 : list(map(lambda mm1,mm2 : mm1+mm2,m1,m2)) ,matrix1,matrix2))

# f9([[1,0],[0,1]],[[1,0],[0,1]])
# f9([[1,2,3],[4,5,6]],[[-1,-1,-1],[-1,-1,-1]])
# f9([[1],[2],[3],[4]],[[4],[3],[2],[1]])
