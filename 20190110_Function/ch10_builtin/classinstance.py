class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age


a = person('yuchan',34)
print(isinstance(a,person))
print(isinstance(a,object))


pystring = 'Python'
sobject = slice(3)

my_list = [4,7,0,3]
my_iter = iter(my_list)

while True:
    v = next(my_iter)
    if v!=None:
        print(v)
    else:
        break

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

myfunclist = [add,mul]
myfunclist[0](3,4)
myfunclist[1](3,4)


items = [1,2,3,4,5]
squared = list(map(lambda x:x**2,items))

ii = {1:3,2:4,3:6}
ss = list(map(lambda x,y:x*y,ii.keys(),ii.values()))