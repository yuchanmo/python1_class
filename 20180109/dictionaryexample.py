# find within dictionary
stateMap = {'pit':'PA','chi':'IL','seattle':'WA','boston':'MA'}

city = input('Enter a city Name').lower()
if city in stateMap :
    print(city.title(),"is in",stateMap[city])
else:
    print('Sorry,never heard of it')


# typing 한 숫자들을 counting 하는 예제

counts = dict()
while True:
    n = int(input('Enter an integer (0 to end) -->'))
    if (n==0):
        break
    if (n in counts):
        counts[n] += 1
    else:
        counts[n] = 1
    print('I have seen',n,'a total of',counts[n],'time(s)')
print('done,counts:',counts)


a = {'name':'pkey','phone':'01012312','birth':'1118'}
a.keys()