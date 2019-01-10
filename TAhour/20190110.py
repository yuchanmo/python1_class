bicycle = ['trek','cannondale','readline']
message = 'my first bicycle was a ' + bicycle[0].title() + "."
print(message)


motorcycle = ["honda",'yamaha',"suzuki",'ducati']
print(motorcycle)

motorcycle.remove('ducati')
print(motorcycle)


#reverse
cars = ['bmw','audi','toyota','subaru']

print(cars)
print(sorted(cars))
print(sorted(cars,reverse = True))
print(cars)

#title
m = ['alice','david','carno']
for i in m:
    print(i.title())

#even_number
even_num = list(range(2,11,2))
print(even_num)

#square.
sq = []

for value in range(2,11):
    s = value**2
    sq.append(s)
print(sq)

#players
p = ['charles','martina','mike','eli']
for pl in p[:3]:
    print(pl.title())


#tuple
d = (200,50)
print(d)

#if
cars = ['audi','bmw','sabaru','toyota']
for c in  cars:
    if c =='bmw':
        print(c.title())
    else:
        print(c)



age = 13
if age <4 :
    p = 0
elif age < 14:
    p = 1
print(p)


pets =['dog','cat','dog','goldfish','cat','rabbit','cat']

while 'cat' in pets:
    pets.remove('cat')
print(pets)