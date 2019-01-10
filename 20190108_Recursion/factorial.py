def factorial_iter(n):
    result  = 1
    for i in range(1,n+1):
        result = result * i

    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n*factorial_recursive(n-1)

def factorial(n,depth = 0):
    print('depth,')
    if(n<2):
        result = 1
    else:
        result = n * factorial(n-1,depth+1)
    print('*depth=>',result)
    return result