import array

s1 = 'this is the array'

a = array.array('u',s1)
print(a)
a.append('dfsd')
print(a)

print(a.count('i'))


s1 = 'This is the array,haha'

a = array.array('u',s1)
print(a)
a.index('h')
print(a)


a.insert(50,'W')
a[49]



#array module application

from array import array

a = array('i')

a.append(100)
a.append(200)
a.append(300)

print('Original : ',a)
a.insert(1,900)
print('Insert(1,900) : ',a)

a.remove(200)
print('Remove(200) : ',a)
a.count(900)