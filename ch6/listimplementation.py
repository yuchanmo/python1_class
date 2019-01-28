import copy

L = [1,2,3]
A = L
S = copy.copy(L)


def printarrayList():
    print(L)
    print(A)
    print(S)

printarrayList()

L.pop()
printarrayList()
L[1] = 5
printarrayList()