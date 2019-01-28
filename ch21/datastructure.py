l = [3,7,1]
l.append(5)
l


from array import *
a = array('i',[4,3,6])
a


a.append(5)
a

b = array(1,2,3)
b
b.append(4)
b

from abc import ABC,abstractmethod

class a(ABC):

    @abstractmethod
    def abmethod(self):
        pass


class b(a):
    def __init__(self,ddd,eee):
        self.ddd = ddd
        self.eee = eee
    
    def abmethod(self):
        return super().abmethod()



class Node:
    def __init__(self,contents=None,next =None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)

def print_list(node):
    while node:
        print(node.getContents())
        node= node.next
    print()

def testList():
    node1 = Node('Car')
    node2 = Node('bus')
    node3 = Node('lorry')
    node1.next = node2
    node2.next= node3
    print_list(node1)

testList()


mylist = [1,2,3,4,5]

i = iter(mylist)
print(next(i))


class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]



class Stack:

    def __init__(self,*args):
        self.items = []
        if len(args) != 0:
            self.items.extend(args)
        

    def push(self,d):
        self.items.append(d)

    def pop(self,d):
        try:

            return self.items.pop()
        except IndexError as ie:
            print('There is no item in stack anymore')
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items)-1]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.items == []:
            print('there is no iterable item in this class')
        v = self.items[self.index]
        self.index +=1 
        return v



t =(1,2,3,4,5,6)
mys = Stack(*t)

    
it = iter(mys)
print(it.__next__())



class Queue:
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def delete(self):
        itemToDelete = self.items[0]
        del self.items[0]
        return itemToDelete

    def size(self):
        return len(self.items)

    def report(self):
        return self.items

myq = Queue()
myq.add('Bob')
myq.add('Brodie')
myq.add('carrie')
myq.add('Tanya')

print(myq.size())
print(myq.report())
print(myq.delete())
print(myq.report())


aaa= array()


import queue

a = queue.Queue(5)
b = queue.Queue(3)

a.put(1)
a.put('Python')
a.put(b)

b.put(3)
print(a.get())
print(a.get())
print(a.get().get())

b = queue.LifoQueue(5)
c = queue.PriorityQueue(5)


b.put(1)
b.put(2)
b.put(3)


import queue

a = queue.Queue(3)
b = queue.Queue()

a.put(1)
a.put(2)
a.put(3)

a.get()
a.get()
a.get()



import queue

a = queue.PriorityQueue(3)

a.put(20)
a.put(1)
a.put(9)

a.qsize()

a.get()
a.qsize()
a.get()
a.get()

list(map(hash,range(1,6)))



from hashlib import *

md5('a'.encode('utf-8')).digest()