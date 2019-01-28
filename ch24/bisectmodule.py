from bisect import bisect
import random

lst = [10,20,30,40,50]
print(lst)

bisect(lst,21)
bisect(lst,19)
bisect(lst,8)


from bisect import bisect
grades = 'FEDCBA'
breakpoint = [30,44,66,75,85]
def grade(total):
    return grades[bisect(breakpoint,total)]

grade(66)

grade_map = map(grade,[33,99,77,44,12,88])
list(map(print,grade_map))


bkp = ['b','e','u','x']
bisect(bkp,'ssdfs')


import collections



rrr = [chr(random.randint(1,26) + ord('a')) for i in range(30)]
rrr = collections.Counter(map(lambda x : bisect(bkp,x),rrr))




import queue

a = queue.PriorityQueue()

a.put((0,'sdf'))
a.put((1,'abc'))
a.put((10,'sdfs'))
a.put((-3,'sdfsdf'))
a.get()
