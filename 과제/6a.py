#1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle.1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1. Write a function f1(n) that prints the following triangle. 1.
def f1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

#2
def f2(n):
    cnt = 0
    for i in range(1,n+1):
        for j in range(i):
            cnt+=1
            print(cnt,end=' ')
        print()

#3
def f3(n):
    rowcnt = (n-1)*2 + 1
    start = 1
    prestart = start    
    iterange = 0
    for i in range(1,rowcnt+1):
        if i<=n:
            iterange+=1 
        else:
            iterange-=1
            start = prestart - iterange
        prestart = start
        for j in range(iterange):
            print(start,end=' ')
            start+=1
        print()
        



#4
def f4(n):
    rowcnt = (n-1)*2 + 1
    start = 1
    iterange = 0
    for i in range(1,rowcnt+1):
        iterange = iterange+1 if i<=n else iterange-1
        for j in range(iterange):
            print(start,end=' ')
            start+=1
        print()

#5
def f5(matrix):
    def sumofrow(lst):
        sum = 0
        for l in lst:
            sum += l
        print(sum)
    for row in matrix:
        sumofrow(row)

#6
def f6(matrix):
    for i in range(len(matrix)):
        print(matrix[i][i])


#7
def f7(matrix):
    for row in matrix:
        sum = 0
        for a in row:
            sum+=a
        print(sum)

#8
def f8(matrix):
    sum = 0
    for row in matrix:
        for a in row:
            sum+=a
    return sum

#9
def f9(matrix):
    res = 1
    for row in matrix:
        for a in row:
            res *=a
    return res


#10
def f10(matrix):
    for row in matrix:
        for a in row:
            if a % 2 ==1 :
                print(a,end =' ')
        print()

#11
def f11(matrix1,matrix2):
    outerarray = []
    for idx1 in range(len(matrix1)):
        innerarray = []
        m1 = matrix1[idx1]
        m2 = matrix2[idx1]
        for idx2 in range(len(matrix1[idx1])):
            res = m1[idx2] + m2[idx2]
            innerarray.append(res)
        outerarray.append(innerarray)
    return outerarray

#12
def f12(matrix1,matrix2):
    outerarray = []
    for rowidx in range(len(matrix1)):
        innerarray = []
        m1 = matrix1[rowidx]   
        for lenmat2 in range(len(matrix2[0])):               
            tmpsum = 0
            for colidx in range(len(m1)): 
                tmpsum+=m1[colidx]*matrix2[colidx][rowidx]
            innerarray.append(tmpsum)
        outerarray.append(innerarray)            
    return outerarray

#13
def f13(matrix):
    m = matrix
    is_identity = True
    for rowidx in range(len(matrix)):
        for colidx in range(len(matrix)):
            v =  m[rowidx][colidx]
            if rowidx == colidx:
                is_identity &= v==1
            else:
                is_identity &= v==0
    return is_identity


# #14
# def f14(rows,cols):
#     outerarray = []
#     for r in range(rows):
#         innerarray = []
#         for c in range(cols):
#             if r == 0 or r == (rows-1):
#                 if c == 0 or c == (cols-1):
#                     innerarray.append(2)
#                 else:
#                     innerarray.append(3)
#             else:
#                 if c == 0 or c == (cols-1):
#                     innerarray.append(3)
#                 else:                    
#                     innerarray.append(4)
#         outerarray.append(innerarray)
#     return outerarray


f12([[4,3,2,1]],[[1],[2],[3],[4]])

