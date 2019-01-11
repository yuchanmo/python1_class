
def bsearch(items,key):
    return bs_helper(items,key,-1,len(items))


def bs_helper(items,key,lower,upper):
    if lower + 1 == upper:
        return None
    mid = (lower + upper) // 2
    if key == items[mid]:
        return mid
    if key < items[mid]:
        return bs_helper(items,key,lower,mid)
    else:
        return bs_helper(items,key,mid,upper)


items = list(range(1000))

print(bsearch(items,10))
