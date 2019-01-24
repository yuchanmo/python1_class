import queue

a = queue.Queue(3)
b= queue.LifoQueue(5)
c = queue.PriorityQueue(5)
d = queue.Queue(5)


a.put(1)
a.put('python')
a.put(d)

d.put(3)

a.full()
print(a.get())
print(a.get())
print(a.get().get())


#deque

import queue

a = queue.Queue(3)
a.put('kim')
a.put(55)
a.put('snu')
a
a.qsize()

a.get()
a.qsize()

import queue

a = queue.PriorityQueue(3)
a.put(20)
a.put(1)
a.put(9)
a.qsize()

a.get()
a.qsize()
a.get()
a.qsize()
