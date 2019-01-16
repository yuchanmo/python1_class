#ch7 recursive

#최대공약수
def gcd(x,y):
    while y >0:
        tmp_x = x
        x = y
        y = tmp_x % y
    return x


def gcd_recursive(x,y):
    if y == 0:
        return x
    return gcd_recursive(y,x%y)


gcd(20,12)
gcd_recursive(20,12)


#fibonacci

def fibo(n):
    x = 0
    y = 1
    for i in range(n):
        x,y = y, x+y
    return x

def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)


fibo(10)
fibo_recursive(10)

#reverse
def reverseString(s):
    res = ''
    for i in range(len(s)-1,-1,-1):
        res = res + s[i]
    return res

def reverseStringRecursive(s):
    if s == '':
        return s
    return s[-1] + reverseStringRecursive(s[:-1])

teststring = "hello"
reverseString(teststring)
reverseStringRecursive(teststring)


#mergesort
def mergelist(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return lst1 + lst2
    if lst1[0] < lst2[0]:
        return lst1[:1] + mergelist(lst1[1:],lst2)
    else:
        return lst2[:1] + mergelist(lst1,lst2[1:])

def mergesort(lst):
    if len(lst) <=1 :
        return lst
    halfidx = len(lst) // 2
    l1 = mergesort(lst[ :halfidx])
    l2 = mergesort(lst[halfidx: ])
    sorted_list = mergelist(l1,l2)
    return sorted_list


testlist = [3,6,1,9,4,8,7]
mergesort(testlist)

def loopPower(a,n):
    res = 1
    for i in range(n):
        res = res * a
    return res

def loopPowerRecursive(a,n):
    if n == 0:
        return 1
    return a * loopPowerRecursive(a,n-1)

def recursivePower(a,n):
    if n==0:
        return 1
    else:
        factor = recursivePower(a,n//2)
        if n%2==0:
            return factor * factor
        else:
            return factor * factor * a


loopPower(3,3)
loopPowerRecursive(3,3)
recursivePower(3,3)


#selection sort
def recursiveSummation(n):
    if n == 0:
        return 0
    return 1/(n*n) + recursiveSummation(n-1)


def calculatePi(n):
    return (6*recursiveSummation(n))**0.5

calculatePi(100)



