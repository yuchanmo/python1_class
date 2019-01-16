

# with open('newfile.txt','w') as f:
#     list(map(lambda a : f.write('line number is %s \n'%(a) ),range(30)))




f = open('newfile.txt','r')
f.readlines()


cnt = 0
while cnt <3:
    line = f.readline()
    if line == '':
        f.seek(0,0)
        cnt+=1
    print(line,end='')

f.close()


with open('pipi.txt','r') as f2:
    for line in f2:
        print(line.strip())



print(f2.read())


def calpi(n):
    assert n > 0
    if n == 1:
        return 1
    return 1/(n**2) + calpi(n-1)

def getpi(n):
    assert n > 0
    return (calpi(n)*6)**0.5


getpi(990)

list(map(lambda x : print('%s : %s '%(x,eval('1E-'+str(x)))),range(100)))



from decimal  import *
getcontext().prec = 6
Decimal(1) / Decimal(6)

getcontext().prec = 28
Decimal(1) / Decimal(7)
a = 0.1234567823456752354435345353423434234234234
a


fn = 'c:/yuchan/programming.txt'

with open(fn,'a') as ff:
    for i in range(500,600):
        ff.write(str(i))
        ff.write('\n')


rfn = 'test.txt'
d = dict()
with open(rfn,'r') as fff:
    for line in fff:
        a = line.strip().split(',')
        d[a[0]] = a[1:]

print(d)


l = [["bob","kim","moyu"],["bob","kim","moyu"],["bob","kim","moyu"]]

import csv
rfn = 'a.txt'
with open(rfn,'w+') as cf:
    fr = csv.writer(cf)
    fr.writerows(l)




try:
    f = open('foos.txt','r')
    print('heelo')
except Exception as e:
    print('error occured')
else:
    print('nice to meet you')
finally:
    print('this line should be excuted')

def divideval(v,n):
    try:
        return v//n
    except ZeroDivisionError as ze:
        print('can`t divide with zero')
    except Exception as ge:
        print('unknown error occured')
    else:
        print('done to divide')
    finally:
        print('BOA')

divideval(10,3)
divideval(10,0)


    


def getQuadratic(a,b,c):
    try:
        rt = (b**2 - 4*a*c)**0.5
        r1 = (-b +rt)/2*a
        r2 = (-b -rt)/2*a
        return (r1,r2)
    except Exception as er:
        print('unknown error occured')


getQuadratic(10,3,4)

