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


