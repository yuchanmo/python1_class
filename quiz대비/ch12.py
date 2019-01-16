import random as r

r.randint(1,100)

testset = []

def gt():        
    global testset
    testset = ([r.randint(1,100) for i in range(10)])
    r.shuffle(testset)
    print(testset)

def selectionsort(lst):
    if lst == 0:
        return lst
    mi = 0
    for i in range(len(lst)-1):
        minval = lst[i]
        for j in range(i,len(lst)):
            if lst[j] < minval:
                mi = j
                minval = lst[j]
        lst[i],lst[mi] = lst[mi],lst[i]
    return lst

print(testset)

selectionsort(testset)


def insertionsort(lst):
    for i in range(1,len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j],lst[j-1] = lst[j-1],lst[j]
            j-=1


def bubblesort(lst):
    for i in range(0,len(lst)-1):
        for j in range(i,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

gt()
bubblesort(testset)



def mergelist(lst1,lst2):
    if len(lst1)==0:
        return lst2
    if len(lst2)==0:
        return lst1
    else:
        if lst1[0] < lst2[0]:
            return lst1[:1] + mergelist(lst1[1:],lst2)
        else:
            return lst2[:1] + mergelist(lst1,lst2[1:])

def mergesort(lst):
    #두개로 쪼갠다
    #쪼갠데이터를 비교해서 합친다
    hi = len(lst)//2
    if len(lst)<=1 :
        return lst
    
    l1 = mergesort(lst[:hi])
    l2 = mergesort(lst[hi:])
    res = mergelist(l1,l2)
    return res


mergelist([1,3,5],[2,4,6])

gt()
mergesort(testset)


def bssearch(lst,key):
    return bs_helper(lst,key, -1,len(lst))

def bs_helper(lst,key,lower,upper):
    if lower + 1== upper:
        return None

    mid = (lower + upper) //2
    if key == lst[mid]:
        return mid
    if key < lst[mid]:
        return bs_helper(lst,key,lower,mid)
    else:
        return bs_helper(lst,key,mid,upper)


l = list(range(3,10))
bssearch(l,3)

    