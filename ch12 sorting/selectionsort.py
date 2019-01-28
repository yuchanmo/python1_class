
def selectionsort(items):
    for i in range(len(items)-1):
        mi = i
        for j in range(i+1,len(items)):
            if items[j] < items[mi]:
                mi = j
        items[mi],items[i] = items[i],items[mi]
    return items


a = [5,4,1,6,7,2]

print(selectionsort(a))