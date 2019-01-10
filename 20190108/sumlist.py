def sumlist(items):
    if len(items) == 0 :
        return 0   
    return items[0] + sumlist(items[1:])

