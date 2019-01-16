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



#ch8 tuple/set/dictionary
s1 = set([1,2,3])
s2 = set([2,3,4])

s1&s2
s1|s2
s1-s2

s1.add(5)
s1
s1.remove(5)
s1

s3 = {'a','b','c'}
s4 = s3.copy()
s3
s3.add('d')
s3
s4

s1^s2

{'c'}.issuperset(s3)


di = {(1,2):3,(4,5):6}
len(di)
ei = di.copy()
ei[(5,6)] = 7
di
ei

#ch9 copy/deep copy
import copy
a = [1,5,9,[33,23,23,[235,565]]]
b= copy.copy(a)
c= copy.deepcopy(a)
d = list(a)
e = a + []
f = a[:]

a[2] = 40
a[3][1]=60
a[3][3][1] = 999
print(a,b,c,d,e,f)

ddd = {(1,2):3,{1:4}:3}

a = list(range(1,5))
b= list(range(5,22))
c = zip(a,b)
d = [(aa,bb) for aa,bb in c]
d


#12 soring and searchnig
def binarySearch(lst,v):
    return bsHelper(lst,v,-1,len(lst))

def bsHelper(lst,v,lower,upper):
    if lst == []:
        return None
    half = (lower + upper) // 2
    
    half_val = lst[half]
    if v == half_val:
        return half
    elif half_val > v:
        return bsHelper(lst,v,lower,half)
    else:
        return bsHelper(lst,v,half,upper)
    

binarySearch([1,2,3,4,5,6,7,8,9],4)


def quickSort(lst):
    if len(lst)<=1:
        return lst
    
    pivot_idx = len(lst)//2
    smaller_items = []
    larger_items =[]
    for i,v in enumerate(lst):
        if i!=pivot_idx:
            if v < lst[pivot_idx]:
                smaller_items.append(v)
            else:
                larger_items.append(v)
    quickSort(smaller_items)
    quickSort(larger_items)
    lst[:] = smaller_items + [lst[pivot_idx]] + larger_items



