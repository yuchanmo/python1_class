import random


list(map(lambda x : random.random(),range(1000)))

def positive(x):
    return x > 0


n = range(-5,5)
less_than_zero = list(filter(lambda x:x<0,n))