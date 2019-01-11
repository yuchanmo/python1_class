def insertion_sort(items):
    res = []
    for i in range(len(items)):
        minval = items[i]
        for j in range(i+1,len(items)):
            if items[j] < minval : 
                minval = items[j]
        res.append(minval)
    return res

a = [5,4,1,6,7,2]

print(insertion_sort(a))