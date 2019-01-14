#LCG Formula
# x = (ax + c) % m
# a = 1 , c  = 7, m = 12

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



# 주사위 random

import random as r

def roll_die():
    roll = prng() %6 + 1
    assert 1 <= roll and roll <=6
    return roll


def election_year():
    election_number = prng()%((2012-1788)//4+1)



def roll():
    from random import randint
    return randint(1,6)

def DiceStat(trials):
    c_list = [0]*11
    c_prob = [0]*11

    for i in range(trials):
        v1 =roll()
        v2 = roll()
        d_idx = v1+v2 -2
        c_list[d_idx] = c_list[d_idx] + 1
    
    for j in range(0,11):
        c_prob[j] = c_list[j]/trials
        print("probability for ",j+2,":",c_prob[j])


DiceStat(10000)


def HungryDice():
    cnt=0
    saved_money = 0
    while cnt<3:        
        v1 = roll()
        v2 = roll()       
        if v1 == v2:
            cnt += 1
        else:
             saved_money += v1 + v2
        
    return saved_money



HungryDice()
        
def avg_winnings(runs):
    total = 0
    for n in range(runs):
        total += HungryDice()
    return total/runs


avg_winnings(10000)


[round(avg_winnings(10),2) for i in range(5)]
[round(avg_winnings(100),2) for i in range(5)]
[round(avg_winnings(1000),2) for i in range(5)]
[round(avg_winnings(10000),2) for i in range(5)]
[round(avg_winnings(100000),2) for i in range(5)]



import random
def gggikki(n):
    answer = [4,1,5,2,3]        
    tryans =list(range(1,6))
    random.shuffle(tryans)
    return sum(list(map(lambda x,y : x == y,tryans,answer)))

gggikki(3)


from random import shuffle

def student(pairs,samples):
    num_correct = 0
    matching = list(range(pairs))
    for i in range(samples):
        shuffle(matching)
        for j in range(pairs):
            if matching[j] == j:
                num_correct = num_correct + 1
    return num_correct / samples


def quandary(p):
    assert p <=1 and p >=0
    import random
    location = 0
    umbrella = [1,1]    
    wet = False
    walk_cnt = 0
    while wet==False:
        if random.random()< p:
            if umbrella[location] == 0:
                wet = True
            else:
                walk_cnt += 1
                umbrella[location] -=1
                location = 1- location
                umbrella[location] +=1
        else:
            walk_cnt = walk_cnt + 1
            location = 1 - location
    return walk_cnt

for i in range(0,100):     
    p = i*0.01   
    trips = [quandary(p) for i in range(1)]
    avg = sum(trips)/len(trips)
    print("probablity",i," avg : ", avg)



