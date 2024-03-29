from functools import reduce

def f1(n):
    list(map(lambda x:print(*range(1,x+1)), range(1,n+1)))

# f1(5)
# f1(0)
# f1(1)

def f2(n):
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(1,n+1)))

# f2(3)

# f2(0)
# f2(1)
# f2(5)

def f3(n):
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(1,n+1)))
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(n-1,0,-1)))

# f3(3)
# f3(4)
# f3(0)
# f3(1)

def f4(n):
    list(map(lambda x:print(*range(1+sum(range(x)),1+sum(range(x))+x)), range(1,n+1)))
    list(map(lambda x:print(*range(1+sum(range(n+1)) + sum(range(n-1,x,-1)),1+sum(range(n+1))+sum(range(n-1,x,-1))+x)), range(n-1,0,-1)))

# f4(3)
# f4(0)
# f4(1)


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


def f10(matrix1,matrix2):
  if len(matrix2[0])==1:
    return [sum(map(lambda k : matrix1[0][k]*matrix2[k][0] , range(len(matrix1[0]))))]
  else:
    return list(map( lambda i : list(map(lambda j : sum(map(lambda k : matrix1[i][k]*matrix2[k][j] , range(len(matrix1[0])))), range(len(matrix2[0])))), range(len(matrix1))))



# f10([[1,0],[0,1]],[[1,0],[0,1]])
# f10([[1,2,3],[4,5,6]],[[-1,-1],[-1,-1],[-1,-1]])
# f10([[4,3,2,1]],[[1],[2],[3],[4]])

def f11(matrix):
  return all(map(lambda i : matrix[i][i]==1 and sum(matrix[i])==1 , range(len(matrix))))

# f11([[1]])
# f11([[1,0,0],[0,1,0],[0,0,1]])
# f11([[1,0,0],[0,1,5],[0,0,1]])

def f12(rows,cols):     
     # 로직 : rows x cols x idx(-1,1) 의 배열 생성 |row+/-idx| <boundry 의 True 갯수(int로 형변환), |col+/-idx| < boundry 의 형변환
     return list(map(lambda pair : list(map(lambda x : sum(x) ,pair)), list(map(lambda r : list(map(lambda c: list(map(lambda i: int(r+i>-1 and r+i<rows) + int(c+i>-1 and c+i <cols) ,range(-1,2,2))) ,range(cols))),range(rows)))))

# f12(3,3)
# f12(5,1)
# f12(5,0)
# f12(0,5)
# f12(2,2)
