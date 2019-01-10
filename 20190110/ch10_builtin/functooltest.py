from functools import reduce

v = list(range(1,101))

r = reduce(lambda x,y:x+y,v)
p = reduce(lambda x,y:x*y,v)
print(p)
print(r)


