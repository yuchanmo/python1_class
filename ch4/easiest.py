def mole():
    print('enter values ')
    c = eval(input('carbon:'))
    h = eval(input('hydrogen:'))
    o = eval(input('oxygen:'))

    w = c*12.011 + h*1.0079 + o*15.9994
    print('mole weight of c',c,"h",h,"o",o,"is : ",round(w,2))

mole()