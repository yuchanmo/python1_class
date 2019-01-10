import copy


# just 2d
l = [[1,2,3],[4,5,6]]

a = l
s = copy.copy(l)
d = copy.deepcopy(l)

def printresult():
    global a,s,d
    print(a)
    print(l)
    print(s)
    print(d)

printresult()
a[0][1]=100
printresult()


#1+2d 
l = [1,[4,5,6]]
a = l
s = copy.copy(l)
d = copy.deepcopy(l)

printresult()
a[1][2] = 100
printresult()
s[0] = 9
printresult()