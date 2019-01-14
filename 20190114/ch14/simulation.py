#LCG Formula

current_x = 0

def prng_seed(s):
    global current_x
    current_x = 8

def prng1(n):
    return (n+7)%12

def prng():
    global current_x
    current_x = prng1(current_x)
    return current_x


for i in range(10):
    print(prng())