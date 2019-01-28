import math

math.ceil(10)
math.pi
math.e
math.inf
math.nan

a = math.pi*0.5
math.degrees(a)
math.radians(180)

math.sinh(math.pi)

import statistics as s

s.mean([1,2,3,4])


import random

random.seed(2)

for i in range(10000):
    a = random.random()
    print(a)


random.seed(2)
a = random.random()
random.seed(2)
b = random.random()
print(b)
b = random.random()
print(a)
print(b)


random.uniform(3,10)
random.randint(3,10)
random.randrange(10)
random.randrange(0,15,5)


from copy import deepcopy

a = "abcdefghij"
b = [1,2,3,4,5,6,7]
c = deepcopy(b)
b

random.shuffle(b)
b
c
random.choice(a)
random.choice(a)
random.choice(a)
random.choice(a)


c = [1,2,3,4,5]

random.choice(a)
b
random.sample(c,3)



data = [4,2,5,9,7]
data.pop(3)


import random
def random_pop(data):
    number = random.randint(0,len(data)-1)
    return data.pop(number)

if __name__ =='__main__':
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))
