#prng(pseudo random number generator)
c_x = 4
a = 1103515245
c = 12345
m = 2**32
def prng_seed(s):
    global c_x
    c_x = s

def prng1(n):
    return (a*n + c) % m

def prng():
    global c_x
    c_x = prng1(c_x)
    return c_x

list(map(lambda x : prng(),range(20)))


[prng() for n in range(1000)]



#random module

import random as r

# randrange(b) : range와 같은 범위내에서 random 값 생성
# randint(a,b) : a<=x<=b 내에서 integer random 값 생성
# uniform(a,b) : a<=x<=b a에서 b사이의 float 값 생성
# random() : 0~1 사이 float 값 생성




[r.randrange(10) for i in range(20)]
[r.uniform(1,10) for i in range(5)]
[r.random() for i in range(100)]

[r.randint(0,99) for i in range(100)]
[r.randint(1,100) for i in range(100)]



colors = ['red','blue','green','gray','black']
print(colors)
r.shuffle(colors)
print(colors)

[r.sample(colors,2) for i in range(10)]
[r.choice(colors) for i in range(10)]



#dice game

def roll_die():
    roll = prng() % 6 +1
    assert 1 <= roll and roll <=6
    return roll

[roll_die() for i in range(100)]


#election
def election_year():
    election_number = prng() % ((2012 - 1788)//4+1)
    assert 0 <= election_number and election_number <=56
    year = election_number * 4 + 1788
    assert 1788 <=year and year <= 2012 and year %4 ==0
    return year

[election_year() for i in range(5)]
set([prng() % ((2012 - 1788)//4+1) for i in range(100)])


def diceStat(trials):
    c_list = [0]*11
    c_prob = [0]*11

    for i in range(trials):
        v1 = roll_die()
        v2 = roll_die()
        print(v1,v2)
        d_i = v1 + v2 - 2
        c_list[d_i] = c_list[d_i]+ 1
    
    for j in range(0,11):
        c_prob[j]  = c_list[j] / trials * 0.1
        print('The probablity for ',j+2,":",c_prob[j])

diceStat(100)


def probDice(trials):
    cl = {i:0 for i in range(1,13)}
    cpl = {i:0 for i in range(1,13)}

    for i in range(trials):
        v1 = r.randint(1,6)
        v2 = r.randint(1,6)
        di = v1+v2
        cl[di]+=1
    
    for k,v in cl.items():
        print('sum of dice : %s, probability : %s'%(k,v/trials))

[probDice(10000) for i in range(5)]


def dice_game():
    strike = 0
    winning_money = 0
    while strike < 3:
        d1 = r.randint(1,6)
        d2 = r.randint(1,6)
        if d1 == d2:
            strike+=1
        else:
            winning_money+=(d1+d2)
    return winning_money

def avg(lst):
    assert len(lst) > 0
    return sum(lst)/len(lst)

[avg([dice_game() for i in range(50)]) for k in range(10)]

def student(pairs,samples):
    n_correct = 0
    matching = list(range(pairs))
    for i in range(samples):
        r.shuffle(matching)
        for j in range(pairs):
            if matching[j] == j:
                n_correct += 1
    return n_correct / samples



def wetgame(p):
    location = 0
    umb = [1,1]
    wet = False
    cnt = 0
    while wet == False:
        rain_prob = r.random() * 100
        cnt+=1
        if rain_prob < p:
            if umb[location] == 0:
                wet = True
                break
            else:
                umb[location] -= 1
                location = 1 if location ==0 else 0
                umb[location] += 1
        else:
            location = 1 if location ==0 else 0
    return cnt

[wetgame(i) for i in range(1,100)]


