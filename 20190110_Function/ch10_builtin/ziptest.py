a = list(range(1,6))
b= list(map(lambda x : chr(ord('a') + x),range(5)))

for x,y in zip(a,b):
    print(x,y)