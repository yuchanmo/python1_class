import math

def quadratic5():
    print('this program finds the real solutions to a quadratic\n')

    try:
        a,b,c = eval(input('please enter coeff'))
        discRoot = math.sqrt(b*b-4*a*c)
    except ValueError as ve:
        print('crash')

quadratic5()