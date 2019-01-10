def msort(list):
    if len(list) ==0 or len(list) == 1:
        return list[:len(list)]

    halfway = len(list)//2
    list1 = list[0:halfway]
    list2 = list[halfway:len(list)]
    newlist1 = msort(list1)
    newlist2 = msort(list2)
    newlist = merge(newlist1,newlist2)
    return newlist

def merge(a,b):
    index_a = 0
    index_b = 0
    c = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            c.append(a[index_a])
            index_a = index_a + 1
        else:
            c.append(b[index_b])
            index_b = index_b + 1
    
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c


testset = [1,5,6,7,23,25,353,21,12,4]
res = msort(testset)
print(res)