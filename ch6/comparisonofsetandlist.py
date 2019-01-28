"is".lower()
import time as t

n = 1000
a = list(range(2,n+1,2))

def calculateperformanceofarray():
    global n,a
    print('Using a list...',end = "")
    start = t.time()
    count = 0
    for x in range(n+1):
        if x in a : 
            count += 1

    end = t.time()
    elapsed1 = end - start
    print('count = ',count," and time=%0.4f seconds"%elapsed1)


def calculateperformanceofset():
    global n,a
    start = t.time()
    s = set(a)
    count = 0
    for x in range(n+1):
        if x in s:
            count += 1
    end = t.time()
    elasped2 = end - start
    print('count = ',count," and time=%0.4f seconds"%elasped2)


calculateperformanceofarray()
calculateperformanceofset()